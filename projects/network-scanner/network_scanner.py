"""
Network scanner that scans the network for all devices connected
to it using the ICMP protocol.
"""


import argparse
import re
import signal
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

from termcolor import colored


def def_handler(sig, frame):
    print(colored("\n[!] Exiting the program.\n", "red"))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Network Scanner that discovers active hosts in a network (ICMP)"
    )
    parser.add_argument(
        "-t",
        "--target",
        required=True,
        dest="target",
        help="Target IP / IP range",
    )
    args = parser.parse_args()
    return args.target


def parse_target(target):
    splitted_target = target.split(".")
    first_three_octets = ".".join(splitted_target[:3])
    last_octet = splitted_target[-1]

    if "-" in last_octet:
        start, end = last_octet.split("-")
        targets = [
            f"{first_three_octets}.{o}" for o in range(int(start), int(end) + 1)
        ]
        return targets
    else:
        return [target]


def validate_target(target):
    if re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", target):
        return True
    elif re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}-\d{1,3}", target):
        return True
    else:
        return False


def host_discovery(target):
    try:
        ping = subprocess.run(
            f"ping -c 1 {target}",
            timeout=3,
            stdout=subprocess.DEVNULL,
            shell=True,
        )
        if ping.returncode == 0:
            print(colored(f"[+] {target} is up", "green"))
        else:
            print(colored(f"[-] {target} is down", "red"))
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        print(colored(f"[-] {target} is down", "red"))


def main():
    target = get_arguments()
    if not validate_target(target):
        raise ValueError("Invalid target IP / IP range")
    targets = parse_target(target)
    print(colored(f"\n[*] Scanning {target}...", "green"))
    print(colored(f"\n[*] Targets to scan: {targets}", "grey"))
    print(colored("\n[*] Scanning started...", "green"))
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(host_discovery, targets)
    print(colored("\n[*] Scanning completed...", "green"))


if __name__ == "__main__":
    main()
