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
  
  # Check the contents of the file and run the appropriate script
  if [[ $contents == "Solo" ]]; then
    # If the "Solo" command is received, stop the "auto.sh" script if it's running
    if $is_running && [[ $prev_command != "Solo" ]]; then
      echo "Stopping xauto.sh..."
      pid=$(pgrep -f "astrominer")
      kill "$pid"
      is_running=false
    fi

    echo "Starting zolo.sh..."
    ./zolo.sh &
    is_running=true
    prev_command="Solo"
  elif [[ $contents == "Auto" ]]; then
    # If the "Auto" command is received, stop the "solo.sh" script if it's running
    if $is_running && [[ $prev_command != "Auto" ]]; then
      echo "Stopping zolo.sh..."
      pid=$(pgrep -f "astrominer")
      kill "$pid"
      is_running=false
    fi
    
    echo "Starting xauto.sh..."
    ./xauto.sh &
    is_running=true
    prev_command="Auto"
  fi

  # Wait for 1 minute before checking again
  sleep 60
done
