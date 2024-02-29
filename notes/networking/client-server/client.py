import socket


def start_client():
    host = "localhost"
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            message = input("[+] Introduce tu mensaje: ")
            s.sendall(message.encode())
            if "bye" in message:
                break
            data = s.recv(1024)
            print(f"[+] Server answer: '{data.decode()}'")


start_client()
