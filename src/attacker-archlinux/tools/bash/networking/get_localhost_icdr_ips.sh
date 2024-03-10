#!/bin/bash

# The script tries to collect all the local IP addresses of the
# host machine, exluding the loopback one

# First try to get the local ICDR-IP addresses from the `ip` command
if [ -z "$ICDR_IP" ]; then
    ICDR_IP=$(ip -o -4 addr list 2>/dev/null | awk '{print $4}')
fi

# Then try to get the local ICDR-IP addresses from the `ip` command
if [ -z "$ICDR_IP" ]; then
    IP_AND_MASK=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2 "/" $4}')
    ICDR_IP=$(ipcalc -n -b "$IP_AND_MASK" 2>/dev/null | grep Network | awk '{print $2, $3}')
fi

# Filter loopback address
ICDR_IP=$(echo "$ICDR_IP" | grep -v "127.0.0.1")

if [ -z "$ICDR_IP" ]; then
    ICDR_IP="<UNABLE_TO_COLLECT_ICDR_IP>"
fi

echo "$ICDR_IP"
