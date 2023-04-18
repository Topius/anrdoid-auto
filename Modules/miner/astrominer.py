import os

import subprocess
import time
from Modules.System import *

# Define the ADB command with the path to the ADB executable
# adb_command = "E:\\Top\\Android\\platform-tools\\adb.exe"
# SCRCPY_PATH = "E:\\Top\\Android\\scrcpy-win64-v1.25\\scrcpy.exe"
# astro_patch = "https://github.com/dero-am/astrobwt-miner/releases/download/V1.8_BETA5/astrominer-V1.8_BETA5_F_aarch64_linux.tar.gz"

# Start scrcpy with USB device selection
#scrcpy_process = subprocess.Popen([SCRCPY_PATH, "--select-usb"])

rm_astro()
# subprocess.run([adb_command, "shell", "input", "text", "rm"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "astrominer"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
rm_rpc()
# subprocess.run([adb_command, "shell", "input", "text", "rm"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "rpc_mining.sh"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

rm_astro_tab()
# subprocess.run([adb_command, "shell", "input", "text", "rm"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "astro"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_TAB"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

rm_astro_tab()
# subprocess.run([adb_command, "shell", "input", "text", "rm"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "astro"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_TAB"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

wget_astro()
# subprocess.run([adb_command, "shell", "input", "text", "wget"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", astro_patch])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "--no-check-certificate"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
# time.sleep(7)
# subprocess.run([adb_command, "shell", "input", "text", "tar"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "-xf"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "ast"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_TAB"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

wget_auto()
# subprocess.run([adb_command, "shell", "input", "text", "wget"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "https://raw.githubusercontent.com/Topius/anrdoid-auto/main/auto.sh"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

executable_auto()
# subprocess.run([adb_command, "shell", "input", "text", "chmod"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "+x"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "auto.sh"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

# run_auto()
# subprocess.run([adb_command, "shell", "input", "text", "./auto.sh"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])



# subprocess.run([adb_command, "shell", "input", "text", "rpc"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])