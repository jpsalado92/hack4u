import tkinter as tk

root = tk.Tk()
root.title("Frame() Widget")

frame = tk.Frame(root, bg="blue", bd=5)

frame.place(relx=0.5, rely=0.5, anchor="center")

label1 = tk.Label(frame, text="Hello World 1!", bg="red")
label2 = tk.Label(frame, text="Hello World 2!", bg="green")
label1.pack()
label2.pack()

root.mainloop()