#!/bin/bash

# The script tries to collect all the local MAC addresses of the
# host machine, exluding the loopback one

# First try to get the local MAC addresses from the `ip` command
if [ -z "$MAC" ]; then
    MAC=$(ip addr show 2>/dev/null | grep link | awk '{print $2}') 
fi

# If the `ip` command fails, try to get the MAC address from the `ifconfig` command
if [ -z "$MAC" ]; then
    MAC=$(ifconfig 2>/dev/null | grep "ether " | awk '{print $2}')
fi

# If the `ifconfig` command fails, try to get the MAC address from the `hostname` command
if [ -z "$MAC" ]; then
    MAC=$(cat /sys/class/net/*/address 2>/dev/null)
fi

# Filter loopback address
MAC=$(echo "$MAC" | grep -v "00:00:00:00:00:00")

# Format the MAC addresses
MAC=$(echo "$MAC" | cut -d/ -f1 | tr '\n' ' ' | sed 's/ $//')

echo "$MAC"
