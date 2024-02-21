"""
We require ifconfig to be installed on the system.

utils: macchanger -s eth0  # Show the current MAC address
utils: macchanger -l  # List all available interfaces
"""

import argparse
import re
import signal
import socket
import subprocess
import sys

from termcolor import colored


def def_handler(sig, frame):
    print(colored("\n[!] Exiting the program.\n", "red"))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def get_arguments():
    parser = argparse.ArgumentParser(description="MAC changer.")
    parser.add_argument(
        "-i",
        "--interface",
        dest="interface",
        required=True,
        help="Interface to change MAC (Ex: -i eth0)",
    )
    parser.add_argument(
        "-m",
        "--mac",
        dest="mac",
        required=True,
        help="MAC to change to (Ex: -m 00:11:22:33:44:55)",
    )
    options = parser.parse_args()
    return options.interface, options.mac


def get_available_interfaces():
    return socket.if_nameindex()


def is_valid_interface(interface):
    interface_is_available = any(
        [interface == i[1] for i in get_available_interfaces()]
    )
    return interface_is_available


def is_valid_mac(mac):
    return bool(re.match(r"([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}", mac))


def change_mac_address(interface, mac):
    previous_mac = subprocess.check_output(
        ["ip", "link", "show", interface]
    ).decode()
    previous_mac = re.search(
        r"ether ([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}", previous_mac
    )
    previous_mac = (
        previous_mac.group(0).replace("ether", "").strip()
        if previous_mac
        else None
    )
    print(
        f"[+] Changing MAC address of {interface} from {previous_mac} to {mac}."
    )
    # Down the interface
    subprocess.run(["ip", "link", "set", "dev", interface, "down"])
    # Change MAC (hw stands for hardware)
    subprocess.run(["ip", "link", "set", "dev", interface, "address", mac])
    # Up the interface
    subprocess.run(["ip", "link", "set", "dev", interface, "up"])


def main():
    interface, mac = get_arguments()
    if not is_valid_interface(interface):
        print(f"[+] Interface `{interface}` is not available.")
    elif not is_valid_mac(mac):
        print(f"[+] MAC `{mac}` is not valid.")
    else:
        change_mac_address(interface, mac)


main()
