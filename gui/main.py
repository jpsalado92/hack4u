import tkinter as tk

# Main tab of the application
root = tk.Tk()

# Set the title of the application
root.title("Python GUI")


label = tk.Label(root, text="Hello World", bg="red")
label.pack()
button = tk.Button(root, text="Exit", command=root.quit, bg="black", fg="white")
button.pack(fill=tk.X, side=tk.BOTTOM)

# Start the application
root.mainloop()
