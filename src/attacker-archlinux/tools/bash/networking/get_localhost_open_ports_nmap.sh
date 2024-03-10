#!/bin/bash

function ctrl_c(){
  echo -e "\n\n[!] Closing...\n"
  tput cnorm; exit 1
}

# Ctrl+C
trap ctrl_c INT
tput civis  # Hide cursor

nmap -p- --open localhost

tput cnorm  # Show cursor again
