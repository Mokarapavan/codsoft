import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        self.master.geometry("600x600")
        self.master.configure(bg="white")

        self.expression = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        display_frame = tk.Frame(self.master, bg="white")
        display_frame.pack(pady=20)

        display_label = tk.Label(display_frame, textvariable=self.result_var, font=("Helvetica", 24), bg="white", width=15, anchor="e")
        display_label.pack(fill="x", padx=10, pady=10)

        button_frame = tk.Frame(self.master, bg="white")
        button_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(button_frame, text=text, font=("Helvetica", 20), width=10, height=3, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=10, pady=10)

    def on_button_click(self, text):
        if text == 'C':
            self.expression = ""
        elif text == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += text

        self.result_var.set(self.expression)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
