import subprocess
from Modules.System import *

# adb_command = "E:\\Top\\Android\\platform-tools\\adb.exe"
# SCRCPY_PATH = "E:\\Top\\Android\\scrcpy-win64-v1.25\\scrcpy.exe"

# Start scrcpy with USB device selection
scrcpy_process()
input_enter()

# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_CTRL_LEFT"])
# subprocess.run([adb_command, "shell", "input", "text", "C"])

rm_auto()
# subprocess.run([adb_command, "shell", "input", "text", "rm"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "auto.sh"])

wget_auto()
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
# subprocess.run([adb_command, "shell", "input", "text", "wget"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "https://raw.githubusercontent.com/Topius/anrdoid-auto/main/auto.sh"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "--no-check-certificate"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

executable_auto()
# subprocess.run([adb_command, "shell", "input", "text", "chmod"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "+x"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "auto.sh"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

run_auto()
# subprocess.run([adb_command, "shell", "input", "text", "./auto.sh"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])