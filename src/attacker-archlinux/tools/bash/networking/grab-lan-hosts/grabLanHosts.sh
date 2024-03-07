#!/bin/bash

# Create a script in bash that lists all the active hosts in the current network
# with nmap

# Check if nmap is installed
if ! [ -x "$(command -v nmap)" ]; then
  echo 'Error: nmap is not installed.' >&2
  exit 1
fi

# Get the current network
network=$(ip route | grep -oP 'default via \K\S+') && network=${network%.*}

# Get the active hosts
nmap -sn $network.0/24 | grep -oP '\d+\.\d+\.\d+\.\d+'
```

