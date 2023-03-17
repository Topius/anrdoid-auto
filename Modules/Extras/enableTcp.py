import os

import subprocess
import time
from Modules.path import adb_command, SCRCPY_PATH

# Define the ADB command with the path to the ADB executable
# adb_command = "E:\\Top\\Android\\platform-tools\\adb.exe"
# SCRCPY_PATH = "E:\\Top\\Android\\scrcpy-win64-v1.25\\scrcpy.exe"

# Start scrcpy with USB device selection
scrcpy_process = subprocess.Popen([SCRCPY_PATH, "--select-usb", "--tcpip"])
time.sleep(5)
#subprocess.run([adb_command, "shell", "input", "text", "done"])


