import json
import os
import sqlite3

# Update the saved player nickname without changing any other profile data.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "Database", "Files", "player.sqlite")
NEW_NAME = "СільодкінаВкусняшка"

def main():
    if not os.path.isfile(DB_PATH):
        print("Nickname update: player database not found; skipping.")
        return

    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT ID, Data FROM main")
        rows = cursor.fetchall()

        changed = 0
        for player_id, raw_data in rows:
            try:
                data = json.loads(raw_data)
                if data.get("Name") != NEW_NAME:
                    data["Name"] = NEW_NAME
                    cursor.execute(
                        "UPDATE main SET Data=? WHERE ID=?",
                        (json.dumps(data, ensure_ascii=False), player_id)
                    )
                    changed += 1
            except (TypeError, ValueError):
                continue

        conn.commit()
        print("Nickname update complete. Profiles updated:", changed)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
