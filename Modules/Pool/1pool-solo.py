import os
import subprocess
import time
from Modules.System import adb_command, SCRCPY_PATH

# # Define the ADB command with the path to the ADB executable
# adb_command = "E:\\Top\\Android\\platform-tools\\adb.exe"
# SCRCPY_PATH = "E:\\Top\\Android\\scrcpy-win64-v1.25\\scrcpy.exe"

# Start scrcpy with USB device selection
scrcpy_process = subprocess.Popen([SCRCPY_PATH, "--select-usb"])

subprocess.run([adb_command, "shell", "input", "text", "./auto.sh"])
subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

# subprocess.run([adb_command, "shell", "input", "text", "./astrominer"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "-w"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "dero1qyxacd6a0xsxxdp5vwlf0hk585znc405wp5ga7g0vrcxzm665ysksqq5lv307"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "-r"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "dero-node-overlode.mysrv.cloud:10300"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "-p"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "rpc"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
#
#
# #./astrominer -w dero1qyxacd6a0xsxxdp5vwlf0hk585znc405wp5ga7g0vrcxzm665ysksqq5lv307 -r dero-node-overlode.mysrv.cloud:10300 -p rpc