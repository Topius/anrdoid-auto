#!/bin/bash

# URL of the file on Github
url="https://raw.githubusercontent.com/Topius/anrdoid-auto/main/command.txt"

# Variable to store the currently running script
running_script=""

# Function to stop the currently running script
stop_running_script() {
  if [[ "$running_script" == "solo" ]]; then
    # Send SIGINT signal to stop the solo.sh script
    pkill -SIGINT solo.sh
  elif [[ "$running_script" == "auto" ]]; then
    # Send SIGINT signal to stop the auto.sh script
    pkill -SIGINT auto.sh
  fi
}

# Loop indefinitely
while true; do
  # Download the file from Github
  contents=$(curl -sSL $url)

  # Check the contents of the file and run the appropriate script
  if [[ $contents == "Solo" ]]; then
    stop_running_script
    running_script="solo"
    ./solo.sh &
  elif [[ $contents == "Auto" ]]; then
    stop_running_script
    running_script="auto"
    ./auto.sh &
  fi

  # Wait for 5 minutes before checking again
  sleep 300
done
