import socket


def start_client():
    host = "localhost"
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            data = s.recv(1024)
            print(f"[server]: '{data.decode()}'")
            message = input("[client]: ")
            s.sendall(message.encode())
            if "bye" in message:
                break


start_client()
