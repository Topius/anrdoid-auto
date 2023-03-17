import os

import subprocess
import time
from path import adb_command, SCRCPY_PATH

# # Define the ADB command with the path to the ADB executable
# adb_command = "E:\\Top\\Android\\platform-tools\\adb.exe"
# SCRCPY_PATH = "E:\\Top\\Android\\scrcpy-win64-v1.25\\scrcpy.exe"

# # Define the user and password for the new user
# new_user = input("New User: ")
# new_password = input("New Pass: ")

# Start scrcpy with USB device selection
#scrcpy_process = subprocess.Popen([SCRCPY_PATH, "--select-usb"])

#Open SSh Config

subprocess.run([adb_command, "shell", "input", "text", "sudo"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "nano"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "/etc/ssh/sshd_config"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

print('---------------------')
input("Confirm Port Change Press Enter")
print('---------------------')
#Start SSH Service

subprocess.run([adb_command, "shell", "input", "text", "sudo"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "service"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "ssh"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "start"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

#Check SSH Service

subprocess.run([adb_command, "shell", "input", "text", "sudo"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "service"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "ssh"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "status"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

subprocess.run([adb_command, "shell", "input", "text", "exit"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
