#!/bin/bash

should_restart=true

# Set up signal handler for SIGINT and SIGTERM
trap 'should_restart=false; echo "Stopping astrominer..."; pkill -TERM astrominer' SIGINT SIGTERM

while $should_restart; do
  ./astrominer -w dero1qyxacd6a0xsxxdp5vwlf0hk585znc405wp5ga7g0vrcxzm665ysksqq5lv307 -r dero-node.mysrv.cloud:10300 -p rpc
  
  # Check if astrominer exited normally
  exit_status=$?
  if [ $exit_status -eq 0 ]; then
    echo "astrominer has exited normally, restarting in 5 seconds..."
    sleep 5
  else
    if $should_restart; then
      echo "astrominer has crashed or exited abnormally, sleeping for 5 seconds before restarting..."
      sleep 5
    else
      echo "astrominer was stopped manually with CTRL+C, not restarting."
    fi
  fi
done
