import socket
import threading
import ssl


def broadcast(message, client_socket, clients, prefix=""):
    for c in clients:
        if c != client_socket:
            c.send(f"{prefix}{message}".encode("utf-8"))


def handle_client(conn, addr, clients, usernames):
    print(f"\n[!] New connection from {addr}\n")
    conn.send(
        "Welcome to the chat server! Please enter a username:".encode("utf-8")
    )
    username = conn.recv(1024).decode("utf-8")
    clients.append(conn)
    usernames[conn] = username
    # print(f"Username of the client is {username}")
    broadcast(
        message=f"{username} has joined the chat!",
        client_socket=conn,
        clients=clients,
        prefix="[server]: ",
    )
    conn.send(f"Connection successful!\nWelcome {username}\n".encode("utf-8"))

    while True:
        try:
            message = conn.recv(1024).decode("utf-8")

            if message == "list":
                conn.send("Listing all users...".encode("utf-8"))
                conn.send(" ".join(usernames.values()).encode("utf-8"))
            elif message == "quit":
                conn.send("Quitting...".encode("utf-8"))
                conn.close()
                clients.remove(conn)
                broadcast(
                    message=f"`{username}` has left the chat.",
                    client_socket=conn,
                    clients=clients,
                    prefix="[server]: ",
                )
                break
            elif message:
                broadcast(
                    message=message,
                    client_socket=conn,
                    clients=clients,
                    prefix=f"[{username}]: ",
                )
            else:
                pass

        except Exception as e:
            print(e)
            conn.close()
            clients.remove(conn)
            broadcast(
                message=f"`{username}` has left the chat.",
                client_socket=conn,
                clients=clients,
                prefix="[server]: ",
            )
            print(f"\n[!] {addr} has disconnected")
            break


def server_program():
    host = "localhost"
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server-cert.pem", keyfile="server-key.key")

    server_socket = context.wrap_socket(server_socket, server_side=True)
    server_socket.listen()
    print("Server is listening for connections...")
    clients = []
    usernames = {}

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(
            target=handle_client, args=(conn, addr, clients, usernames)
        )
        thread.daemon = (
            True  # Daemon threads will close when the main thread closes
        )
        thread.start()


server_program()
