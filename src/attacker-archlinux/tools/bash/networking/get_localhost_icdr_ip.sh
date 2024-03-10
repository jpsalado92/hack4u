#!/bin/bash

# Run the script "get_localhost_icdr_ips.sh" which is next to this file
ICDR_IP=$(bash ./get_localhost_icdr_ips.sh)

# Grab the first line of the ICDR-IP addresses
ICDR_IP=$(echo "$ICDR_IP" | head -n 1)

echo "$ICDR_IP"
