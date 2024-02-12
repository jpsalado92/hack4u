import socket
import threading

from tkinter import Tk, Entry, BOTH, Frame, Button
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

HOST = "localhost"
PORT = 12345

def receive_message(client_socket, text_widget):
    """
    Receive messages from the client socket and write them to the chat window.

    Args:
        client_socket (socket): The client socket to receive messages from.
        text_widget (Widget): The text widget to write the messages to.

    Returns:
        None
    """
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                write_to_chat_window(data.decode(), text_widget)
        except Exception as e:
            write_to_chat_window(text=e, text_widget=text_widget)

def send_message(client_socket, entry_widget, text_widget, window):
    text = entry_widget.get()
    entry_widget.delete(0, tk.END)
    write_to_chat_window("> " + text, text_widget=text_widget)
    client_socket.sendall(text.encode())
    if text.lower() == "quit":
        window.destroy()
    

def write_to_chat_window(text, text_widget):
    text_widget.configure(state='normal')
    text_widget.insert(tk.END, "\n" + str(text))
    text_widget.configure(state='disabled')

def start_client():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        window = Tk()
        window.title("Chat")
        text_widget = ScrolledText(window, state="disabled")
        text_widget.pack(padx=5, pady=5)
        frame_widget = Frame(window)
        frame_widget.pack(pady=5, padx=5, fill=BOTH, expand=1)
        entry_widget = Entry(frame_widget)
        entry_widget.bind(
            sequence="<Return>",
            func=lambda _: send_message(
                client_socket=s,
                entry_widget=entry_widget,
                text_widget=text_widget,
                window=window
            ),
        )
        entry_widget.pack(fill=BOTH, expand=1, side=tk.LEFT)
        button_widget = Button(frame_widget, text="Send", padx=5)
        button_widget.pack(side=tk.RIGHT)

        thread = threading.Thread(target=receive_message, args=(s, text_widget))
        thread.daemon= True
        thread.start()

        window.mainloop()

start_client()
