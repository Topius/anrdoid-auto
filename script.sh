#!/bin/bash

# URL of the file on Github
url="https://raw.githubusercontent.com/Topius/anrdoid-auto/main/command.txt"

# Variable to keep track of the current process
current_process="none"

# Function to stop the current process
function stop_current_process {
  if [ "$current_process" != "none" ]; then
    echo "Stopping $current_process..."
    killall $current_process
    current_process="none"
  fi
}

# Set up signal handler for SIGINT (CTRL+C)
trap 'stop_current_process; exit 0' SIGINT

# Loop indefinitely
while true; do
  # Download the file from Github
  contents=$(curl -sSL $url)

  # Check the contents of the file and run the appropriate script
  if [[ $contents == "Solo" ]]; then
    # Stop the current process if it's not the solo script
    if [ "$current_process" != "solo.sh" ]; then
      stop_current_process
    fi

    # Start the solo script if it's not already running
    if [ "$current_process" != "solo.sh" ]; then
      echo "Starting solo.sh..."
      ./solo.sh &
      current_process="solo.sh"
    fi
  elif [[ $contents == "Auto" ]]; then
    # Stop the current process if it's not the auto script
    if [ "$current_process" != "auto.sh" ]; then
      stop_current_process
    fi

    # Start the auto script if it's not already running
    if [ "$current_process" != "auto.sh" ]; then
      echo "Starting auto.sh..."
      ./auto.sh &
      current_process="auto.sh"
    fi
  fi

  # Wait for 5 minutes before checking again
  sleep 300
done
