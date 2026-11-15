# LSBS V46 - GitHub updater for Pydroid 3
# Updates server files from the main branch while preserving local settings and player data.

import os
import shutil
import tempfile
import urllib.request
import zipfile

REPO_ZIP = "https://codeload.github.com/foodkyoto0-crypto/LSBS-V46-Custom/zip/refs/heads/main"

ROOT = os.path.dirname(os.path.abspath(__file__))
SKIP_DIRS = {".git", "__pycache__", "Database"}
SKIP_FILES = {"Configuration.py", "update_server.py"}

def should_skip(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    if any(part in SKIP_DIRS for part in parts):
        return True
    if parts[-1] in SKIP_FILES:
        return True
    if any(part.startswith("HexDump") for part in parts):
        return True
    return False

def main():
    print("===================================")
    print("       LSBS V46 GITHUB UPDATE")
    print("===================================")
    print("Downloading latest files from GitHub...")

    request = urllib.request.Request(
        REPO_ZIP,
        headers={"User-Agent": "LSBS-V46-Pydroid-Updater"}
    )

    with tempfile.TemporaryDirectory() as temp:
        archive_path = os.path.join(temp, "server.zip")
        extract_dir = os.path.join(temp, "extract")
        os.makedirs(extract_dir, exist_ok=True)

        with urllib.request.urlopen(request, timeout=60) as response:
            with open(archive_path, "wb") as file:
                shutil.copyfileobj(response, file)

        print("Extracting update...")
        with zipfile.ZipFile(archive_path, "r") as archive:
            archive.extractall(extract_dir)

        source_root = None
        for current, dirs, files in os.walk(extract_dir):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            if "Core.py" in files:
                source_root = current
                break

        if source_root is None:
            raise RuntimeError("Core.py was not found in the downloaded archive.")

        print("Installing updated server files...")
        copied = 0
        for current, dirs, files in os.walk(source_root):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for filename in files:
                source = os.path.join(current, filename)
                rel_path = os.path.relpath(source, source_root)
                if should_skip(rel_path):
                    continue

                destination = os.path.join(ROOT, rel_path)
                os.makedirs(os.path.dirname(destination), exist_ok=True)
                shutil.copy2(source, destination)
                copied += 1

        print("")
        print("UPDATE COMPLETE!")
        print("Updated files:", copied)
        print("Preserved: Configuration.py, Database and HexDump files.")
        print("Now open Core.py in Pydroid 3 and press Run.")

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("")
        print("UPDATE FAILED:", error)
        print("Check your internet connection and try again.")
    input("\nPress Enter to close...")
