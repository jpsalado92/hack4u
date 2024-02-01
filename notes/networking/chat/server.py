import socket
def start_chat_server():
    host = "localhost"
    port = 1234
    # Instantiate the socket for IPV4 (AF_INET) and TCP (SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set socket `SOL_SOCKET` property `SO_REUSEADDR` to 1, to avoid waiting times when reusing connections
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Listen to incoming connections
    server_socket.bind((host, port))

    # Limit of connections at the same time
    server_socket.listen(1)
    print("[+] Server ready for incoming connections...")

    # Accept client connection and use it throgh `connection`
    connection, client_addr = server_socket.accept()
    print(f"[+] Client {client_addr} connected")

    while True:
        client_message = connection.recv(1024).decode()
        print(f"-> Message sent by the client: {client_message}")
        server_message = input()
        if "bye" in client_message:
            break
        print(f"-> Message sent by the server: {server_message}")
        connection.send(server_message.encode())
    connection.close()
        

start_chat_server()