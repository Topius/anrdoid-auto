import os

import subprocess
import time
from path import adb_command, SCRCPY_PATH

# adb_command = "E:\\Top\\Android\\platform-tools\\adb.exe"
# SCRCPY_PATH = "E:\\Top\\Android\\scrcpy-win64-v1.25\\scrcpy.exe"

#wget

subprocess.run([adb_command, "shell", "input", "text", "sudo"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "apt"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "install"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "wget"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
time.sleep(10)
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
time.sleep(15)