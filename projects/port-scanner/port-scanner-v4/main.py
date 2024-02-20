import argparse
from concurrent.futures import ThreadPoolExecutor
import signal
import socket
import sys
from threading import Thread
import time

from termcolor import colored


open_sockets = []


def def_handler(sig, frame):
    print(colored("\n[!] Exiting the program.\n", "red"))
    for s in open_sockets:
        s.close()
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


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
    s.settimeout(1)
    open_sockets.append(s)
    return s


def port_scanner(host, port) -> tuple[int | None, list[str] | None]:
    s = create_socket(port)
    try:
        s.connect((host, port))
        s.sendall(b"HEAD / HTTP/1.1\r\n\r\n")
        response = s.recv(1024)
        response = response.decode(errors="ignore").split("\n")
        if response:
            header = response
        else:
            header = None
        # print(colored(f"\n[+]Port {port} is open\n", "green"))
        s.close()
        open_sockets.remove(s)
        return port, header
    except (socket.timeout, ConnectionRefusedError, socket.gaierror):
        s.close()
        open_sockets.remove(s)
        return None, None


def main():
    target, port = get_arguments()
    ports = get_ports_to_scan(port)
    print(
        colored("[+] Target to scan: ", "yellow"), colored(f"{target}", "green")
    )
    print(colored("[+] Ports to scan: ", "yellow"), colored(f"{port}", "green"))
    simple_scanner(target, ports)
    basic_threading_scanner(target, ports)
    pool_executor_scanner(target, ports)


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


def simple_scanner(target, ports):
    print(colored("\n[+] Simple Scanner:", "cyan"))
    t0 = time.time()
    results = []
    for port in ports:
        results.append(port_scanner(target, port))
    open_ports = [r for r in results if r != (None, None)]
    print_results(t0, open_ports)



def basic_threading_scanner(target, ports):
    print(colored("\n[+] Basic Threading Scanner:", "cyan"))
    t0 = time.time()
    threads = []
    results = []  # List to store the return values
    for port in ports:
        thread = Thread(
            target=lambda: results.append(port_scanner(target, port))
        )
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print_results(t0, results)

def print_results(t0, results):
    open_ports = [r for r in results if r != (None, None)]
    print("    - Open Ports:")
    for op in open_ports:
        print(f"        - {op[0]}")
        if op[1] == [""]:
            continue
        for l in op[1]:
            if not l.strip() == "":
                print(colored(f"            - {l}", "grey"))
    print(f"    - Elapsed Time: {time.time() - t0}\n")


def pool_executor_scanner(target, ports):
    print(colored("\n[+] Pool Executor Scanner:", "cyan"))
    t0 = time.time()
    results = []
    with ThreadPoolExecutor(max_workers=200) as executor:
        for result in executor.map(port_scanner, [target] * len(ports), ports):
            results.append(result)
    open_ports = [r for r in results if r != (None, None)]
    print_results(t0, open_ports)


if __name__ == "__main__":
    main()
