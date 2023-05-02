What is this for?

Miner every minute program Checks for file content on Github in my case command.txt

Auto - if in command.txt it reads Auto then All miners withing 5 minutes(github update delay) will follow command and start mining on pool
Solo - if in command.txt it reads Solo then All miners withing 5 minutes(github update delay) will follow command and start mining on your node
Stop - Stops Mining(have not tested yet)

How to configure it for your usage:
1) In your Github account make file command.txt or name it as you like, in that file you type Auto or Solo or Stop and only.
2) On miner in Astrominer folder download remote.sh !!! with nano remote.sh Change Wallet Address and Pool addresses in Both Solo and Auto mode.
3) run ./remote.sh

Happy mining
