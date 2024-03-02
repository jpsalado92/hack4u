# Grab Local IP Address

You can use the following bash script to get the IP address of your LAN.

## Script

- This script first uses `ifconfig` to get the network information, then uses `grep` to filter for lines containing `"inet "`.
- It **excludes the loopback address (127.0.0.1)** with `grep -v 127.0.0.1`.
- Finally, it uses `awk` to print the second field of the output, which is the IP address.
