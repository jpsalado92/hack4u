#!/bin/bash

# The script tries to collect all the local IP addresses of the
# host machine, exluding the loopback one

# First try to get the local IP addresses from the `ip` command
if [ -z "$IP" ]; then
    IP=$(ip -o -4 addr list 2>/dev/null | awk '{print $4}' | cut -d/ -f1) 
fi

# If the `ip` command fails, try to get the IP address from the `ifconfig` command
if [ -z "$IP" ]; then
    IP=$(ifconfig 2>/dev/null | grep "inet " | awk '{print $2}') 2>/dev/null
fi

# If the `ifconfig` command fails, try to get the IP address from the `hostname` command
if [ -z "$IP" ]; then
    IP=$(hostname -I 2>/dev/null)
fi

# Filter loopback address
IP=$(echo "$IP" | grep -v "127.0.0.1")

# Format the IP addresses
IP=$(echo "$IP" | cut -d/ -f1 | tr '\n' ' ' | sed 's/ $//')

echo "$IP"
