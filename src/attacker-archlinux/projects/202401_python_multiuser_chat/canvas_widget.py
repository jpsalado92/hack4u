import tkinter as tk

root = tk.Tk()
root.geometry("700x800")
root.title("Canvas() Widget")

canvas = tk.Canvas(root, width=250, height=250, bg="blue")

canvas.place(relx=0.5, rely=0.5, anchor="center")

# label1 = tk.Label(canvas, text="Hello World 1!", bg="red")
# label2 = tk.Label(canvas, text="Hello World 2!", bg="green")
# label1.pack()
# label2.pack()
canvas.create_oval(50, 50, 200, 200, fill="red")
canvas.create_line(0, 0, 250, 250, fill="white", width=2)
canvas.create_rectangle(0, 10, 10, 0, fill="white")
root.mainloop()