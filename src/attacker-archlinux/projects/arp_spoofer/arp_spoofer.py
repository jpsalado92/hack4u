# Make the spoofing machine MAC address 00:11:22:33:44:55

import scapy.all as scapy
import time
import sys

# def get_mac(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast/arp_request
#     answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

#     return answered_list[0][1].hwsrc

# We want the router to believe that the MAC address for the victim IP address, is the MAC address of the attacker
# We want the victim to believe that the MAC address for the router IP address, is the MAC address of the attacker