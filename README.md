# anrdoid-auto

Tested on Samsung S8>>>S20+ "Delays are set for S8 so should work on everything above, if trying to use it on slower model you might consider increasing time.sleep(seconds)
MUST CHANGE:
1) in path.py change path to your adb.exe and scracpy.exe
2) in auto.sh file that will be located in same folder as your Astrominer after running process.py(after running leave 2-3min), change Mining address to your address Or it will mine for me :)
you can do it with nano auto.sh  and edit the address line do CTRL+X press Y press enter to save.

Must have
1) Userland > Ubuntu or Termux installed and Open running
2) USB Debugging enabled from Developer mode

python based code After running process.py (Leave it for 2-3 mins)
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
