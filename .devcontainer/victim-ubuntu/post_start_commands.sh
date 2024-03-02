#!/bin/bash
# Get information about the current network
LAN_IP=$(/workspace/src/attacker-archlinux/tools/bash-grab-local-ip/grabLocalIP.sh)
echo "Your local IP address is: $LAN_IP"
NETWORK_IPS=$(/workspace/src/attacker-archlinux/tools/bash-grab-local-ip-ranges/grabLocalIPRanges.sh)
echo "Your network local IPs are: $NETWORK_IPS"