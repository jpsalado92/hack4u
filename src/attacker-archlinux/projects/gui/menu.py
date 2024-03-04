import tkinter as tk
from tkinter import messagebox, filedialog



def custom_action():
    messagebox.showinfo("Custom Action", "You clicked on Custom 1")


root = tk.Tk()
root.title("Menu() Widget")

root.geometry("700x800")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open", command=lambda: filedialog.askopenfilename())
file_menu.add_command(label="Save")
file_menu.add_command(label="Save as")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


custom_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Custom", menu=custom_menu)
custom_menu.add_command(label="Custom 1", command=custom_action)

    
root.mainloop()

