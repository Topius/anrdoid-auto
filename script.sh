#!/bin/bash

should_restart=true
is_running=false
pid=""

# Set up signal handler for SIGINT (CTRL+C)
trap 'should_restart=false; echo "Stopping astrominer..."; kill "$pid"' SIGINT

while $should_restart; do
  # Download the file from Github
  contents=$(curl -sSL "https://raw.githubusercontent.com/Topius/anrdoid-auto/main/command.txt")
  echo "Current contents: $contents"
  echo "Is running: $is_running"

  # Check the contents of the file and run the appropriate command
  if [[ $contents == "Solo" ]]; then
    # If the "Solo" command is received, stop the "Auto" command if it's running
    if $is_running && [[ $prev_command != "Solo" ]]; then
      echo "Stopping astrominer..."
      pid=$(pidof astrominer)
      kill "$pid"
      is_running=false
    fi

    echo "Starting astrominer in Solo mode..."
    ./astrominer -w dero1qyxacd6a0xsxxdp5vwlf0hk585znc405wp5ga7g0vrcxzm665ysksqq5lv307 -r 192.168.5.104:10100 -p rpc &
    is_running=true
    prev_command="Solo"
  elif [[ $contents == "Auto" ]]; then
    # If the "Auto" command is received, stop the "Solo" command if it's running
    if $is_running && [[ $prev_command != "Auto" ]]; then
      echo "Stopping astrominer..."
      pid=$(pidof astrominer)
      kill "$pid"
      is_running=false
    fi
    
    echo "Starting astrominer in Auto mode..."
    ./astrominer -w dero1qyxacd6a0xsxxdp5vwlf0hk585znc405wp5ga7g0vrcxzm665ysksqq5lv307 -r dero-node.mysrv.cloud:10300 -p rpc &
    is_running=true
    prev_command="Auto"
  fi

  # Wait for 1 minute before checking again
  sleep 60
done
