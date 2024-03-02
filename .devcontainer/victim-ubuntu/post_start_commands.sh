#!/bin/bash
# Get information about the current network
LAN_IP=$(hostname -I)
echo "Your local IP address is: $LAN_IP"
echo ""
cat /etc/lsb-release