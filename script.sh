#!/bin/bash

should_restart=true
is_running=false

# Set up signal handler for SIGINT (CTRL+C)
trap 'should_restart=false; echo "Stopping astrominer..."; kill %1' SIGINT

while $should_restart; do
  # Download the file from Github
  contents=$(curl -sSL "https://raw.githubusercontent.com/Topius/anrdoid-auto/main/command.txt")

  echo "Current contents: $contents"
  echo "Is running: $is_running"

  # Check the contents of the file and run the appropriate script
  if [[ $contents == "Solo" ]]; then
    # If the "Solo" command is received, stop the "auto.sh" script if it's running
    if $is_running; then
      echo "Stopping auto.sh..."
      kill %2
      is_running=false
    fi
    
    echo "Starting solo.sh..."
    ./zolo.sh &
    is_running=true
  elif [[ $contents == "Auto" ]]; then
    # If the "Auto" command is received, stop the "solo.sh" script if it's running
    if $is_running; then
      echo "Stopping solo.sh..."
      kill %1
      is_running=false
    fi
    
    echo "Starting xauto.sh..."
    ./xauto.sh &
    is_running=true
  fi

  # Wait for 1 minute before checking again
  sleep 60
done
