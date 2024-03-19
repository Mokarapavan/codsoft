import tkinter as tk
import string
import random

def generate_password():
    password = ""
    length = int(length_entry.get())
    if lowercase_var.get():
        password += string.ascii_lowercase
    if uppercase_var.get():
        password += string.ascii_uppercase
    if numbers_var.get():
        password += string.digits
    if special_var.get():
        password += string.punctuation
    password = ''.join(random.choice(password) for i in range(length))
    password_var.set(password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("800x800")
root.configure(bg='lightgreen')

# Variables
password_var = tk.StringVar()
lowercase_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()

# Labels
tk.Label(root, text="Password Length:", font=('Arial', 20), bg='lightgreen').grid(row=0, column=0, padx=20, pady=20)
tk.Label(root, text="Include Lowercase Letters:", font=('Arial', 20), bg='lightgreen').grid(row=1, column=0, padx=20, pady=20)
tk.Label(root, text="Include Uppercase Letters:", font=('Arial', 20), bg='lightgreen').grid(row=2, column=0, padx=20, pady=20)
tk.Label(root, text="Include Numbers:", font=('Arial', 20), bg='lightgreen').grid(row=3, column=0, padx=20, pady=20)
tk.Label(root, text="Include Special Characters:", font=('Arial', 20), bg='lightgreen').grid(row=4, column=0, padx=20, pady=20)
tk.Label(root, text="Generated Password:", font=('Arial', 20), bg='lightgreen').grid(row=6, column=0, padx=20, pady=20)

# Entry
length_entry = tk.Entry(root, font=('Arial', 20))
length_entry.grid(row=0, column=1, padx=20, pady=20)

# Checkboxes
tk.Checkbutton(root, variable=lowercase_var, bg='lightgreen').grid(row=1, column=1, padx=20, pady=20)
tk.Checkbutton(root, variable=uppercase_var, bg='lightgreen').grid(row=2, column=1, padx=20, pady=20)
tk.Checkbutton(root, variable=numbers_var, bg='lightgreen').grid(row=3, column=1, padx=20, pady=20)
tk.Checkbutton(root, variable=special_var, bg='lightgreen').grid(row=4, column=1, padx=20, pady=20)

# Button
tk.Button(root, text="Generate Password", font=('Arial', 20), command=generate_password).grid(row=5, column=0, columnspan=2, padx=20, pady=20)

# Result label
tk.Label(root, textvariable=password_var, font=('Arial', 20), bg='lightgreen').grid(row=6, column=1, padx=20, pady=20)

root.mainloop()
