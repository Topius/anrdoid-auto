import subprocess
import time
from path import adb_command, SCRCPY_PATH

# Define the ADB command with the path to the ADB executable
# Make sure to INPUT YOUR OWN Path to those files bellow
# adb_command = "E:\\Top\\Android\\platform-tools\\adb.exe"
# SCRCPY_PATH = "E:\\Top\\Android\\scrcpy-win64-v1.25\\scrcpy.exe"

# Start scrcpy with USB device selection
scrcpy_process = subprocess.Popen([SCRCPY_PATH, "--select-usb"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])