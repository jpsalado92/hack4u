import socket

host = input("Enter the host to scan: ")
from_port = int(input("Enter the START of the port range to scan: "))
to_port = int(input("Enter the END of the port range to scan: "))

def create_socket(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    return s

def port_scanner(s, port):
    try:
        s.connect((host, port))  # connect_ex returns 0 if the port is open
        print(f"Port {port} is open")
    except (socket.timeout, ConnectionRefusedError):
        pass



def main():
    for port in range(from_port, to_port):
        s = create_socket(port)
        port_scanner(s=s, port=port)
        s.close()

if __name__ == "__main__":
    main()