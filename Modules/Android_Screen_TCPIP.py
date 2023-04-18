import subprocess
import time
from System import *

# Define the ADB command with the path to the ADB executable
# Make sure to INPUT YOUR OWN Path to those files bellow
# adb_command = "E:\\Top\\Android\\platform-tools\\adb.exe"
# SCRCPY_PATH = "E:\\Top\\Android\\scrcpy-win64-v1.25\\scrcpy.exe"
testcommand = ()


# Start scrcpy with USB device selection
scrapy_tcpip()

    # scrcpy_process = subprocess.Popen([SCRCPY_PATH,"--tcpip"])
    # subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])