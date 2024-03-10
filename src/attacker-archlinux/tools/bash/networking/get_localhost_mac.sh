#!/bin/bash

# Run the script "get_localhost_macs.sh" which is next to this file
MAC=$(bash ./get_localhost_macs.sh)

# Grab the first value of the space separated MAC addresses
MAC=$(echo "$MAC" | awk '{print $1}')

echo "$MAC"
