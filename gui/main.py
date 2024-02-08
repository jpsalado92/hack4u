import tkinter as tk

# Main tab of the application
root = tk.Tk()

# Set the title of the application
root.title("Python GUI")
root.geometry("700x800")
def get_entry_widget_data():
    print(entry_widget.get())

def get_text_widget_data():
    print(text_widget.get("1.0", tk.END))
# Create widgets
label_widget = tk.Label(root, text="Hello World!", bg="red")
entry_widget = tk.Entry(root)
text_widget = tk.Text(root)
button_widget = tk.Button(root, text="Get input data", command=get_text_widget_data)
exit_button = tk.Button(root, text="Exit", command=root.quit, bg="black", fg="white")

# Pack stuff
label_widget.pack(side=tk.TOP)
entry_widget.place(relx=0.5, rely=0.2, anchor="center")
text_widget.place(relx=0.5, rely=0.6, anchor="center")
exit_button.pack(fill=tk.X, side=tk.BOTTOM)
button_widget.pack(fill=tk.X, side=tk.BOTTOM)


# Start the application
root.mainloop()
