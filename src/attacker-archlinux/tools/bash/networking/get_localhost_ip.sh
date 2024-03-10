#!/bin/bash

# Run the script "get_localhost_icdr_ips.sh" which is next to this file
IP=$(bash ./get_localhost_ips.sh)

# Grab the first value of the space separated IP addresses
IP=$(echo "$IP" | awk '{print $1}')

echo "$IP"
