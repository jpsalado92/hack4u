#!/bin/bash

# Get the IP address and subnet mask
IP_AND_MASK=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2 "/" $4}')

# Calculate the IP range
RANGE=$(ipcalc -n -b "$IP_AND_MASK" | grep Network | awk '{print $2, $3}')

# Print the IP range
echo "$RANGE"