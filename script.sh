#!/bin/bash

# Set up signal handler for SIGINT (CTRL+C)
trap 'echo "Stopping astrominer..."; kill $(pgrep astrominer); exit 0' SIGINT

# Start with an empty command
command=""

while true; do
  # Download the file from Github
  contents=$(curl -sSL "https://raw.githubusercontent.com/Topius/anrdoid-auto/main/command.txt")

  # Check if the contents of the file has changed
  if [[ "$contents" != "$command" ]]; then
    # Stop the previous astrominer process if it's running
    if pgrep astrominer; then
      echo "Stopping astrominer..."
      kill $(pgrep astrominer)
    fi

    # Start the new astrominer process with the new command
    if [[ "$contents" == "Solo" ]]; then
      echo "Starting zolo.sh..."
      command="Solo"
      ./zolo.sh &
    elif [[ "$contents" == "Auto" ]]; then
      echo "Starting xauto.sh..."
      command="Auto"
      ./xauto.sh &
    fi
  fi

  # Wait for 5 minutes before checking again
  sleep 60
done
