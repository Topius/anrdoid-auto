import subprocess
from Modules.path import adb_command, SCRCPY_PATH

# adb_command = "E:\\Top\\Android\\platform-tools\\adb.exe"
# SCRCPY_PATH = "E:\\Top\\Android\\scrcpy-win64-v1.25\\scrcpy.exe"

# Start scrcpy with USB device selection
scrcpy_process = subprocess.Popen([SCRCPY_PATH, "--select-usb"])


subprocess.run([adb_command, "shell", "input", "text", "./auto.sh"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])