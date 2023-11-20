#!/bin/bash

greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"

echo -e "\n[+]  My Private IP is: ${greenColour}$(ip a | grep eth | tail -1 | awk '{print $2}' | awk '{print $1}' FS='/')${endColour}\n"