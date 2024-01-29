import socket
import threading

HOST = "localhost"
PORT = 1234


def my_func(*args):
    pass


class MyClientThread(threading.Thread):
    def __init__(self, client_sock, client_addr):
        super().__init__()
        self.client_sock = client_sock
        self.client_addr = client_addr

    def run(self):
        message = ""

        while True:
            data = self.client_sock.recv(1024)
            message = data.decode()

            if "bye" in message:
                break

            print(f"Mensaje enviado por el cliente: {message}")
            self.client_sock.send(data)

        print(f"[+] Client {self.client_addr} desconectado")
        self.client_sock.close()


with socket.socket(
    socket.AF_INET,  # Familia de direcciones IPV4
    socket.SOCK_STREAM,  # Trabajar con conexiones TCP
) as server_socket:
    # A nivel de socket, permitir la reutilización de conexiones recientemente cerradas
    server_socket.setsockopt(
        socket.SOL_SOCKET,  # SOL (Socket Level)
        socket.SO_REUSEADDR,  #  TIME_WAIT
        1,
    )
    server_socket.bind((HOST, PORT))
    print("[+] En espera de conexiones entrantes...")

    while True:
        server_socket.listen(1)
        client_sock, client_addr = server_socket.accept()
        new_thread = MyClientThread(client_sock, client_addr)
        new_thread.start()
