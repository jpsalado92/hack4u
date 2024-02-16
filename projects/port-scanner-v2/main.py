import socket
import argparse
from termcolor import colored
import sys


def get_arguments():
    parser = argparse.ArgumentParser(description="Fast TCP Port Scanner.")
    parser.add_argument(
        "-t",
        "--target",
        dest="target",
        help="Victim target to scan (Ex: -t 192.168.1.1)",
    )
    parser.add_argument(
        "-p",
        "--port",
        dest="port",
        help="Port range to scan (Ex: -p 1-100)",
    )
    options = parser.parse_args()

    if options.target is None or options.port is None:
        parser.print_help()
        sys.exit(1)

    return options.target, options.port

def create_socket(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    return s


def port_scanner(s, host, port):
    try:
        s.connect((host, port))  # connect_ex returns 0 if the port is open
        print(colored(f"\n[+]Port {port} is open\n", "green"))
    except (socket.timeout, ConnectionRefusedError):
        pass


def main():
    target, port = get_arguments()

    ports = get_ports_to_scan(port)

    for port in ports:
        s = create_socket(port)
        port_scanner(s=s, host=target, port=port)
        s.close()

def get_ports_to_scan(port):
    if '-' in port:
        ports = port.split('-')
        return range(int(ports[0]), int(ports[1]) + 1)
    elif ':' in port:
        ports = port.split(':')
        return range(int(ports[0]), int(ports[1]) + 1)
    elif "," in port:
        ports = port.split(',')
        return [int(port) for port in ports]
    else:
        return [int(port)]


if __name__ == "__main__":
    main()
