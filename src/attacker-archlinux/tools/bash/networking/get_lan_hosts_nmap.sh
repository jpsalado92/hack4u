#!/bin/bash

# Get the local host's IP address and CIDR subnet mask
ip_and_cidr=$(./get_localhost_icdr_ip.sh)

# Perform a ping scan with nmap
nmap -sn "$ip_and_cidr"