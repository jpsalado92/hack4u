# Make the spoofing machine MAC address 00:11:22:33:44:55

import scapy.interfaces
import argparse
import time
import sys
from scapy.layers.l2 import arping, ARP, Ether, srp

# def get_mac(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast/arp_request
#     answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

#     return answered_list[0][1].hwsrc

# We want the router to believe that the MAC address for the victim IP address, is the MAC address of the attacker
# We want the victim to believe that the MAC address for the router IP address, is the MAC address of the attacker


def get_lan_active_hosts():
    active_hosts = arping(" ".join(str(scapy.interfaces.ifaces.values())), verbose=0)[0]
    return [host[1].psrc for host in active_hosts]
    
        
    

def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Spoofer")
    parser.add_argument("-t", "--target", dest="ip_address", help="Host / IP Range to Spoof")
    return parser.parse_args()

def main():
    # arguments = get_arguments()
    print(get_lan_active_hosts())

if __name__ == "__main__":
    main()