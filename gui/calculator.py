import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    expression = display.get()
    result = eval(expression)  # This is a security risk, but we dont care for this demo
    display.delete(0, tk.END)
    display.insert(tk.END, result)

root = tk.Tk()
root.title("Advanced Calculator")

# Set the font and size for the buttons and entry field
button_font = ("Arial", 12)
entry_font = ("Arial", 14)

# Set the background color of the calculator
root.configure(bg="#f2f2f2")


display = tk.Entry(root, width=30, borderwidth=5, font=entry_font, justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3)
]

for button_text, row, column in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=10, font=button_font, command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=column, padx=5, pady=5)

clear_button = tk.Button(root, text="C", padx=20, pady=10, font=button_font, command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

equal_button = tk.Button(root, text="=", padx=20, pady=10, font=button_font, command=button_equal)
equal_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
