#!/bin/bash

function ctrl_c(){
  echo -e "\n\n[!] Exiting...\n"
  exit 1
}

# Ctrl+C
trap ctrl_c INT

for i in $(seq 1 254); do
  (nmap -p- --open -T4 192.168.1.$i &>/dev/null) && echo "[+] Host 192.168.1.$i - ACTIVE" &
done; wait