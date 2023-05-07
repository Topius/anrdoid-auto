#!/bin/bash

should_restart=true
is_running=false
pid=""
prev_command=""

# Set up signal handler for SIGINT (CTRL+C)
trap 'should_restart=false; echo "Stopping astrominer..."; kill "$pid"' SIGINT

while $should_restart; do
  # Download the file from Github
  contents=$(curl -sSL -H 'Cache-Control: no-cache' "https://raw.githubusercontent.com/Topius/anrdoid-auto/main/command.txt")
  echo "Current contents: $contents"
  echo "Is running: $is_running"

  if [[ $contents == "Solo" ]]; then
    command="Solo"
  elif [[ $contents == "Auto" ]]; then
    command="Auto"
  else
    command=""
  fi

  if [[ "$command" != "$prev_command" ]]; then
    # If the command has changed, stop the running instance of astrominer
    # and start a new one with the new command
    echo "Stopping astrominer..."
    if $is_running; then
      kill "$pid"
      is_running=false
    fi

    if [[ "$command" == "Solo" ]]; then
      echo "Starting astrominer in Solo mode..."
      ./astrominer -w dero1qyxacd6a0xsxxdp5vwlf0hk585znc405wp5ga7g0vrcxzm665ysksqq5lv307 -r 192.168.5.104:10100 -p rpc &
    elif [[ "$command" == "Auto" ]]; then
      echo "Starting astrominer in Auto mode..."
      ./astrominer -w dero1qyxacd6a0xsxxdp5vwlf0hk585znc405wp5ga7g0vrcxzm665ysksqq5lv307 -r dero-node.mysrv.cloud:10300 -p rpc &
    fi

    pid=$!
    is_running=true
    prev_command="$command"
  fi

  # Wait for 1 minute before checking again
  sleep 60
done
