import os

import subprocess
import time
from System import adb_command, SCRCPY_PATH

# Define the ADB command with the path to the ADB executable
# adb_command = "E:\\Top\\Android\\platform-tools\\adb.exe"
# SCRCPY_PATH = "E:\\Top\\Android\\scrcpy-win64-v1.25\\scrcpy.exe"

# Define the user and password for the new user
new_user = input("New User: ")
new_password = input("New Pass: ")

# Start scrcpy with USB device selection
scrcpy_process = subprocess.Popen([SCRCPY_PATH, "--select-usb"])



subprocess.run([adb_command, "shell", "input", "text", "sudo "])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", "adduser"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

subprocess.run([adb_command, "shell", "input", "text", new_user])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
time.sleep(1)
subprocess.run([adb_command, "shell", "input", "text", new_password])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

subprocess.run([adb_command, "shell", "input", "text", new_password])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])


subprocess.run([adb_command, "shell", "input", "text", "sudo"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
subprocess.run([adb_command, "shell", "input", "text", "usermod"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
subprocess.run([adb_command, "shell", "input", "text", "-aG"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
subprocess.run([adb_command, "shell", "input", "text", "sudo"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
subprocess.run([adb_command, "shell", "input", "text", new_user])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
time.sleep(1)
subprocess.run([adb_command, "shell", "input", "text", "su"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
subprocess.run([adb_command, "shell", "input", "text", "-"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
subprocess.run([adb_command, "shell", "input", "text", "top"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

# #update
# subprocess.run([adb_command, "shell", "input", "text", "apt "])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "update"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
# time.sleep(15)
#
# subprocess.run([adb_command, "shell", "input", "text", "sudo"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "apt"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "upgrade"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
#
# time.sleep(20)
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
# time.sleep(60)

# #wget
#
# subprocess.run([adb_command, "shell", "input", "text", "sudo"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "apt"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "install"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "wget"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
# time.sleep(10)
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
# time.sleep(15)

# #openssh
#
# subprocess.run([adb_command, "shell", "input", "text", "sudo"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "apt"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "install"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "openssh-server"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
# time.sleep(10)
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
# time.sleep(70)
#
# #install nano
#
# subprocess.run([adb_command, "shell", "input", "text", "sudo"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "apt"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "install"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "nano"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
# time.sleep(10)
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
# time.sleep(20)

# #open SSH config
#
# subprocess.run([adb_command, "shell", "input", "text", "sudo"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "nano"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
#
# subprocess.run([adb_command, "shell", "input", "text", "/etc/ssh/sshd_config"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

