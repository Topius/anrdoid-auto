# anrdoid-auto

Tested on Samsung S8>>>S20+ "Delays are set for S8 so should work on everything above, if trying to use it on slower model you might consider increasing time.sleep(seconds)
MUST CHANGE:
1) in path.py change path to your adb.exe and scracpy.exe
2) in System.py Edit astro_patch = "https://github.com/dero-am/astrobwt-miner/releases/download/V1.8_BETA5/astrominer-V1.8_BETA5_F_aarch64_linux.tar.gz" (edit it to current version)
2) in auto.sh file that will be located in same folder as your Astrominer after running process.py(after running leave 20-30min), change Mining address to your address Or it will mine for me :)
you can do it in terminal after installation with nano auto.sh  and edit the address line do CTRL+X press Y press enter to save.

Must have
1) Userland > Ubuntu or Termux installed and !!OPEN!! running
2) USB Debugging enabled from Developer mode

python based code After running process.py (Leave it for 20-33 mins)
1) Waits for your input of new user and password and Creates Admin user 
2) Updates - Upgrades
3) install wget
4) install nano
5) install open Ssh
6) prompt for open SSH port change as 22 dont work (remove # from prompt and modify port)
7) installs Astrominer with auto.sh file in astrominer folder(where you need to change to your address) modifies privilages and makes it executable  
8) Runs (can only be stopped with CTRL+C or if Phone restarts, Else it will restart all the time and try to connect)

After installing do not forget to modify auto.sh with your address and that will be your starting parameter with ./auto.sh

I am not a perfect coder but this works :D
-----------------------------------------------------

!!Bonus!! in Script.sh if you have several phones you can link to a file to a Github in my case Command.txt, Program will check every 1 minute(works in 3-5m)
If in command.txt is written Auto it will mine on Pool, 
If i type in command.txt Solo it will mine on node locally solo
Remember to change in Script.sh:
Wallet Address:
Pool Address:
Local Node Address-Port:

Good Luck
