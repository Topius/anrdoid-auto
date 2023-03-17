import os

import subprocess
import time
from path import adb_command, SCRCPY_PATH

# Define the ADB command with the path to the ADB executable
# adb_command = "E:\\Top\\Android\\platform-tools\\adb.exe"
# SCRCPY_PATH = "E:\\Top\\Android\\scrcpy-win64-v1.25\\scrcpy.exe"

# # Define the user and password for the new user
# new_user = input("New User: ")
# new_password = input("New Pass: ")

# Start scrcpy with USB device selection
#scrcpy_process = subprocess.Popen([SCRCPY_PATH, "--select-usb"])


subprocess.run([adb_command, "shell", "input", "text", "sudo"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "apt"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "install"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "nano"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
time.sleep(10)
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
time.sleep(20)