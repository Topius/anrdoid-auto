import os
import subprocess
import time

adb_command = "E:\\Top\\Android\\platform-tools\\adb.exe"
SCRCPY_PATH = "E:\\Top\\Android\\scrcpy-win64-v1.25\\scrcpy.exe"
astro_patch = "https://github.com/dero-am/astrobwt-miner/releases/download/V1.8_BETA5/astrominer-V1.8_BETA5_F_aarch64_linux.tar.gz"

# Start scrcpy with USB device selection
def scrcpy_process():
    subprocess.Popen([SCRCPY_PATH, "--select-usb"])


def rm_astro():
        subprocess.run([adb_command, "shell", "input", "text", "rm"])
        subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
        subprocess.run([adb_command, "shell", "input", "text", "astrominer"])
        subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

def rm_rpc():
    subprocess.run([adb_command, "shell", "input", "text", "rm"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
    subprocess.run([adb_command, "shell", "input", "text", "rpc_mining.sh"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

def rm_astro_tab():
    subprocess.run([adb_command, "shell", "input", "text", "rm"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
    subprocess.run([adb_command, "shell", "input", "text", "astro"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_TAB"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

# subprocess.run([adb_command, "shell", "input", "text", "rm"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
# subprocess.run([adb_command, "shell", "input", "text", "astro"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_TAB"])
# subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

def wget_astro():
    subprocess.run([adb_command, "shell", "input", "text", "wget"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
    subprocess.run([adb_command, "shell", "input", "text", astro_patch])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
    subprocess.run([adb_command, "shell", "input", "text", "--no-check-certificate"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
    time.sleep(7)
    subprocess.run([adb_command, "shell", "input", "text", "tar"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
    subprocess.run([adb_command, "shell", "input", "text", "-xf"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
    subprocess.run([adb_command, "shell", "input", "text", "ast"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_TAB"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])


#wget auto.sh

def rm_auto():
    subprocess.run([adb_command, "shell", "input", "text", "rm"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
    subprocess.run([adb_command, "shell", "input", "text", "auto"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_TAB"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

def wget_auto():
    subprocess.run([adb_command, "shell", "input", "text", "wget"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
    subprocess.run([adb_command, "shell", "input", "text", "https://raw.githubusercontent.com/Topius/anrdoid-auto/main/auto.sh"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
    subprocess.run([adb_command, "shell", "input", "text", "--no-check-certificate"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

def executable_auto():
    subprocess.run([adb_command, "shell", "input", "text", "chmod"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
    subprocess.run([adb_command, "shell", "input", "text", "+x"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])
    subprocess.run([adb_command, "shell", "input", "text", "auto.sh"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

def run_auto():
    subprocess.run([adb_command, "shell", "input", "text", "./auto.sh"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])




def update():
    subprocess.run([adb_command, "shell", "input", "text", "apt "])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

    subprocess.run([adb_command, "shell", "input", "text", "update"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
    time.sleep(15)

    subprocess.run([adb_command, "shell", "input", "text", "sudo"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

    subprocess.run([adb_command, "shell", "input", "text", "apt"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

    subprocess.run([adb_command, "shell", "input", "text", "upgrade"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

    time.sleep(20)
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
    time.sleep(60)


def install_wget():
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


def install_nano():
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


def install_openssh():
    subprocess.run([adb_command, "shell", "input", "text", "sudo"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

    subprocess.run([adb_command, "shell", "input", "text", "apt"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

    subprocess.run([adb_command, "shell", "input", "text", "install"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

    subprocess.run([adb_command, "shell", "input", "text", "openssh-server"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
    time.sleep(10)
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])
    time.sleep(90)


def conf_openssh():
    subprocess.run([adb_command, "shell", "input", "text", "sudo"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

    subprocess.run([adb_command, "shell", "input", "text", "nano"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

    subprocess.run([adb_command, "shell", "input", "text", "/etc/ssh/sshd_config"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])

    print('---------------------')
    input("Confirm Port Change,CTRL+X>Y>Enter in Linux, Done ? Yes/no Press Enter")
    print('---------------------')


def start_ssh():
    subprocess.run([adb_command, "shell", "input", "text", "sudo"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

    subprocess.run([adb_command, "shell", "input", "text", "service"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

    subprocess.run([adb_command, "shell", "input", "text", "ssh"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_SPACE"])

    subprocess.run([adb_command, "shell", "input", "text", "start"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])


def check_ssh():
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

def scrapy_tcpip():
    subprocess.Popen([SCRCPY_PATH,"--tcpip"])
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])



def input_enter():
    subprocess.run([adb_command, "shell", "input", "keyevent", "KEYCODE_ENTER"])