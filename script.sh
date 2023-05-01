#!/bin/bash

is_running=false
pid=""

# Set up signal handler for SIGINT (CTRL+C)
trap 'echo "Stopping astrominer..."; kill $pid' SIGINT

while true; do
  # Download the file from Github
  contents=$(curl -sSL "https://raw.githubusercontent.com/Topius/anrdoid-auto/main/command.txt")

  echo "Current contents: $contents"
  echo "Is running: $is_running"

  # Check the contents of the file and run the appropriate script
  if [[ $contents == "Solo" ]]; then
    if [[ $is_running == true ]]; then
      echo "Stopping zolo.sh..."
      kill $pid
      is_running=false
    fi
    
    echo "Starting zolo.sh..."
    ./zolo.sh &
    pid=$!
    is_running=true
  elif [[ $contents == "Auto" ]]; then
    if [[ $is_running == true ]]; then
      echo "Stopping xauto.sh..."
      kill $pid
      is_running=false
    fi
    
    echo "Starting xauto.sh..."
    ./xauto.sh &
    pid=$!
    is_running=true
  fi

  # Wait for 1 minute before checking again
  sleep 60
done
