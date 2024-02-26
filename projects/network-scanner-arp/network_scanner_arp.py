"""
Network scanner that scans the network for all devices connected
to it using the ARP protocol.

The command `arp-scan -I ens33 --localnet --ignoredups` can
be used to scan the network for all devices connected to it.

The command `arp -a` can be used to view the ARP table of the
current device.

In order to list network interfaces and their IP addresses, the
command `ip addr` can be used.

"""


import argparse
import re
import signal
import subprocess
import sys

from scapy.layers.l2 import arping, ARP, Ether, srp
from termcolor import colored


def def_handler(sig, frame):
    print(colored("\n[!] Exiting the program.\n", "red"))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Network Scanner that discovers active hosts in a network (ARP)"
    )
    parser.add_argument(
        "-t",
        "--target",
        required=True,
        dest="target",
        help="hostname / Target IP / IP range",
    )
    args = parser.parse_args()
    return args.target


def resolve_target(target):
    if is_ip(target):
        return target
    elif "/" in target:
        host, _range = target.split("/")
        assert int(_range) in range(8, 32)
        if is_ip(host):
            return f"{host}/{_range}"
        else:
            ip = resolve_hostname(host)
            if ip:
                target = f"{ip}/{_range}"
                if is_ip_range(target):
                    return target
            else:
                return False
    else:
        ip = resolve_hostname(target)
        if ip:
            return ip
        else:
            return False


def resolve_hostname(target):
    if target == "localhost":
        return "127.0.0.1"
    else:
        try:
            return (
                subprocess.run(
                    f"getent hosts {target}",
                    shell=True,
                    capture_output=True,
                    text=True,
                )
                .stdout.strip()
                .split(" ")[0]
            )
        except subprocess.CalledProcessError:
            raise ValueError("Invalid hostname")


def is_ip(target):
    return re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", target)


def is_ip_range(target):
    return re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,3}", target)


def scan(ip):
    # 1. Create an ARP request directed to the target IP to get its MAC address
    arp_packet = ARP(pdst=ip)
    # 2. Create an Ethernet frame to send the ARP request
    broadcast_packet = Ether(dst="ff:ff:ff:ff:ff:ff")
    # 3. Combine the Ethernet frame with the ARP request
    arp_packet = broadcast_packet / arp_packet
    # 4. Send the ARP request and receive the response
    answered, unanswered = srp(arp_packet, timeout=1, verbose=0)
    # 5. Print the result, which is a list of tuples (request, response) representing
    # the sent and received packets respectively
    if answered:
        print(colored("\nIP\t\t\tMAC Address\n-----------------------------------------", "green"))
        for _, response in answered:
            print(colored(f"{response.psrc}\t\t{response.hwsrc}", "grey"))
    
    # print(colored(answered, "grey"))


def main():
    target = get_arguments()
    # for target in (
        # "localhost/24",
        # "host.docker.internal/24",
    # ):
    target = resolve_target(target)
    if not target:
        raise ValueError("Invalid target hostname / IP / IP range")
    print(colored(f"\n[*] Scanning {target}...", "green"))
    scan(ip=target)


if __name__ == "__main__":
    main()
