"""
Python server with the `socket` library.
- Listens for incoming connections.
- Once a connection is established, sends back whatever the client submits.
- Drops the connection on 'bye' in the submitted message.
- Accepts multiple client connections at the same time.
- Each new connection is assigned a new thread, so everything can be handled concurrently.
"""

import socket
import threading

HOST = "localhost"
PORT = 1234


class MyClientThread(threading.Thread):
    def __init__(self, client_sock, client_addr):
        super().__init__()
        self.client_sock = client_sock
        self.client_addr = client_addr
        self.client_ip = client_addr[0]
        self.client_port = client_addr[1]

    def run(self):
        print(
            f"[+] Client connected. (`IP:{self.client_ip}`, PORT:`{self.client_port}`)"
        )
        while True:
            data = self.client_sock.recv(1024)
            message = data.decode()

            if "bye" in message:
                break

            print(f"-> Message sent by the client: {message}")
            self.client_sock.send(data)

        print(f"[+] Client {self.client_addr} disconnected")
        self.client_sock.close()


with socket.socket(
    socket.AF_INET,  # Family of IPV4 addresses
    socket.SOCK_STREAM,  # Work with TCP connections
) as server_socket:
    # At SOCKET level, allow for the reutilization of recently closed connections
    server_socket.setsockopt(
        socket.SOL_SOCKET,  # SOL (Socket Level)
        socket.SO_REUSEADDR,  #  TIME_WAIT
        1,
    )
    server_socket.bind((HOST, PORT))
    print("[+] Waiting for incoming connections...")

    while True:
        server_socket.listen(1)
        client_sock, client_addr = server_socket.accept()
        new_thread = MyClientThread(client_sock, client_addr)
        new_thread.start()
