import socket
import threading

HOST = "localhost"
PORT = 1234

def my_func(*args):
    pass

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
        new_thread = threading.Thread(
            target=my_func,
            args=(client_sock, client_addr)
        )
        new_thread.start()
