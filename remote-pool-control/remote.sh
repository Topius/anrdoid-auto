#!/bin/bash

should_restart=true
is_running=false
pid=""

# Set up signal handler for SIGINT (CTRL+C)
trap 'should_restart=false; echo "Stopping astrominer..."; kill "$pid"' SIGINT

while $should_restart; do
  # Check the file from Github  !!!! Make your GITHUB ACCOUNT, and Create file command.txt or any name and Replace link below with it
  contents=$(curl -sSL -H 'Cache-Control: no-cache' "https://raw.githubusercontent.com/Topius/anrdoid-auto/main/remote-pool-control/command.txt")
  echo "Current contents: $contents"
  echo "Is running: $is_running"

  # Check the contents of the file and run the appropriate script
  if [[ $contents == "Solo" ]]; then
    if [[ $prev_command != "Solo" ]]; then
      # If the "Solo" command is received and the previous command was not "Solo",
      # stop the running instance of astrominer and start a new one with the "Solo" command
      echo "Stopping astrominer..."
      if $is_running; then
        kill "$pid"
        is_running=false
      fi

      # !!!!! REPLACE WALLET ADDRESS and your SOLO node IP:Port Below !!!!!!!
      echo "Starting astrominer in Solo mode..."
      ./astrominer -w dero1qyxacd6a0xsxxdp5vwlf0hk585znc405wp5ga7g0vrcxzm665ysksqq5lv307 -r 192.168.5.104:10100 -p rpc &
      pid=$!
      is_running=true
    fi
    prev_command="Solo"
  elif [[ $contents == "Auto" ]]; then
    if [[ $prev_command != "Auto" ]]; then
      # If the "Auto" command is received and the previous command was not "Auto",
      # stop the running instance of astrominer and start a new one with the "Auto" command
      echo "Stopping astrominer..."
      if $is_running; then
        kill "$pid"
        is_running=false
      fi
      
      # !!!!! REPLACE WALLET ADDRESS and your POOL node IP:Port Below !!!!!!!
      echo "Starting astrominer in Auto mode..."
      ./astrominer -w dero1qyxacd6a0xsxxdp5vwlf0hk585znc405wp5ga7g0vrcxzm665ysksqq5lv307 -r dero-node.mysrv.cloud:10300 -p rpc &
      pid=$!
      is_running=true
    fi
    prev_command="Auto"
  fi

  # Wait for 1 minute before checking again
  sleep 60
done
