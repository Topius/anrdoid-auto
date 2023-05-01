#!/bin/bash

should_restart=true
process_id=
previous_command=""

# Set up signal handler for SIGINT (CTRL+C)
trap 'should_restart=false; echo "Stopping astrominer..."; kill $process_id' SIGINT

while $should_restart; do
  # Download the file from Github
  contents=$(curl -sSL "https://raw.githubusercontent.com/Topius/anrdoid-auto/main/command.txt")

  # Check the contents of the file and run the appropriate script
  if [[ $contents == "Solo" ]]; then
    if [[ $previous_command != "Solo" ]]; then
      echo "Starting Solo mode..."
      # Kill the previous process if it's running
      if [[ ! -z "$process_id" ]]; then
        kill $process_id
        sleep 5
      fi
      # Run Solo mode
      ./astrominer -w dero1qyxacd6a0xsxxdp5vwlf0hk585znc405wp5ga7g0vrcxzm665ysksqq5lv307 -r 192.168.5.104:10100 -p rpc &
      process_id=$!
      previous_command="Solo"
    fi
  elif [[ $contents == "Auto" ]]; then
    if [[ $previous_command != "Auto" ]]; then
      echo "Starting Auto mode..."
      # Kill the previous process if it's running
      if [[ ! -z "$process_id" ]]; then
        kill $process_id
        sleep 5
      fi
      # Run Auto mode
      ./astrominer -w dero1qyxacd6a0xsxxdp5vwlf0hk585znc405wp5ga7g0vrcxzm665ysksqq5lv307 -r dero-node.mysrv.cloud:10300 -p rpc &
      process_id=$!
      previous_command="Auto"
    fi
  elif [[ $contents == "Stop" ]]; then
    echo "Stopping astrominer..."
    # Stop the current process
    if [[ ! -z "$process_id" ]]; then
      kill $process_id
      process_id=
    fi
    previous_command=""
  fi

  # Wait for 5 minutes before checking again
  sleep 300
done
