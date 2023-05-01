#!/bin/bash

should_restart=true
process_id=

# Set up signal handler for SIGINT (CTRL+C)
trap 'should_restart=false; echo "Stopping astrominer..."; kill $process_id' SIGINT

while $should_restart; do
  # Download the file from Github
  contents=$(curl -sSL "https://raw.githubusercontent.com/Topius/anrdoid-auto/main/command.txt")

  # Check the contents of the file and run the appropriate script
  if [[ $contents == "Auto" && $(pgrep astrominer) == "" ]]; then
    echo "Starting Auto mode..."
    # Run Auto mode
    ./astrominer -w dero1qyxacd6a0xsxxdp5vwlf0hk585znc405wp5ga7g0vrcxzm665ysksqq5lv307 -r dero-node.mysrv.cloud:10300 -p rpc &
    process_id=$!
  elif [[ $contents == "Solo" && $(pgrep astrominer) == "" ]]; then
    echo "Starting Solo mode..."
    # Run Solo mode
    ./astrominer -w dero1qyxacd6a0xsxxdp5vwlf0hk585znc405wp5ga7g0vrcxzm665ysksqq5lv307 -r 192.168.5.104:10100 -p rpc &
    process_id=$!
  elif [[ $contents == "Stop" ]]; then
    echo "Stopping astrominer..."
    # Stop the current process
    if [[ ! -z "$process_id" ]]; then
      kill $process_id
      process_id=
    fi
  fi

  # Wait for 5 minutes before checking again
  sleep 300
done
