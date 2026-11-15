import os
import sys
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Check GitHub for updates before loading the server.
updater = os.path.join(BASE_DIR, "update_server.py")
if os.path.isfile(updater):
    print("Checking for LSBS V46 updates...")
    result = subprocess.run(
        [sys.executable, updater, "--auto"],
        cwd=BASE_DIR
    )
    if result.returncode != 0:
        print("Auto-update failed; starting with the files already installed.")

import Configuration
from Classes.ServerConnection import ServerConnection
from Static.StaticData import StaticData

dump_dir = os.path.join(BASE_DIR, f"HexDumpV{Configuration.settings['DumpMajor']}")
if not os.path.exists(dump_dir):
    os.mkdir(dump_dir)

StaticData.Preload()

ServerConnection(("0.0.0.0", 9339))
