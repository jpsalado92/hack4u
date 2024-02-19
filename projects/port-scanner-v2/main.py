import socket
import argparse
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from termcolor import colored


def get_arguments():
    parser = argparse.ArgumentParser(description="Fast TCP Port Scanner.")
    parser.add_argument(
        "-t",
        "--target",
        dest="target",
        required=True,
        help="Victim target to scan (Ex: -t 192.168.1.1)",
    )
    parser.add_argument(
        "-p",
        "--port",
        dest="port",
        required=True,
        help="Port range to scan (Ex: -p 1-100)",
    )
    options = parser.parse_args()
    return options.target, options.port


def create_socket(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    return s


def port_scanner(host, port):
    s = create_socket(port)
    try:
        s.connect((host, port))  # connect_ex returns 0 if the port is open
        print(colored(f"\n[+]Port {port} is open\n", "green"))
    except (socket.timeout, ConnectionRefusedError, socket.gaierror):
        pass
    s.close()


def main(use_basic_threading=False, use_thread_pool_executor=False):
    t0 = time.time()
    target, port = get_arguments()
    ports = get_ports_to_scan(port)
    if use_basic_threading:
        basic_threading_scanner(target, ports)
    elif use_thread_pool_executor:
        pool_executor_scanner(target, ports)
    else:
        simple_scanner(target, ports)
    
    print(time.time() - t0)

def pool_executor_scanner(target, ports):
    with ThreadPoolExecutor(max_workers=200) as executor:
        executor.map(lambda port: port_scanner(port, target), ports)

def basic_threading_scanner(target, ports):
    threads = []
    for port in ports:
        thread = Thread(target=port_scanner, args=(target, port))
        threads.append
        thread.start()

        # Wait for all threads to finish
    for thread in threads:
        thread.join()

def simple_scanner(target, ports):
    for port in ports:
        port_scanner(target, port)


def get_ports_to_scan(port):
    if "-" in port:
        ports = port.split("-")
        return range(int(ports[0]), int(ports[1]) + 1)
    elif ":" in port:
        ports = port.split(":")
        return range(int(ports[0]), int(ports[1]) + 1)
    elif "," in port:
        ports = port.split(",")
        return [int(port) for port in ports]
    else:
        return [int(port)]


if __name__ == "__main__":
    main()
