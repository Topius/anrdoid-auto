import os

import subprocess
import time
from System import *

# # Define the ADB command with the path to the ADB executable
# adb_command = "E:\\Top\\Android\\platform-tools\\adb.exe"
# SCRCPY_PATH = "E:\\Top\\Android\\scrcpy-win64-v1.25\\scrcpy.exe"

# # Define the user and password for the new user
# new_user = input("New User: ")
# new_password = input("New Pass: ")

# Start scrcpy with USB device selection
#scrcpy_process = subprocess.Popen([SCRCPY_PATH, "--select-usb"])

install_openssh()

#openssh install
# def install_openssh():
#     subprocess.run([adb_command, "shell", "input", "text", "sudo"])
#     subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
#     subprocess.run([adb_command, "shell", "input", "text", "apt"])
#     subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
#     subprocess.run([adb_command, "shell", "input", "text", "install"])
#     subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
#     subprocess.run([adb_command, "shell", "input", "text", "openssh-server"])
#     subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
#     time.sleep(10)
#     subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
#     time.sleep(90)

# #Start SSH Service
#
# subprocess.run([adb_command, "shell", "input", "text", "sudo"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "service"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "ssh"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "start"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
#
# #Check SSH Service
#
# subprocess.run([adb_command, "shell", "input", "text", "sudo"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "service"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "ssh"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "status"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])


