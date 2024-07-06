import tkinter as tk
from tkinter import messagebox

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("545x500")

        self.expression = ""

        self.input_text = tk.StringVar()

        # Frame for input display
        self.input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.input_frame.pack(side=tk.TOP)

        # Entry widget for displaying input
        self.input_field = tk.Entry(self.input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        self.input_field.pack(ipady=10)

        # Frame for buttons
        self.btns_frame = tk.Frame(self.root, width=400, height=500, bg="black")
        self.btns_frame.pack()

        # Create calculator buttons
        self.create_buttons()

    def create_buttons(self):
        # List of buttons with their labels
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+', 
            'Delete', 'AC', '**', '00'
        ]

        row = 0
        col = 0

        # Loop through buttons list and create each button
        for button in buttons:
            btn = tk.Button(self.btns_frame, text=button, fg="black", width=10, height=3, bd=0, bg="#fff",
                            cursor="hand2", font=('arial', 14, 'bold'), command=lambda x=button: self.on_button_click(x))
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col == 4:
                col = 0
                row += 1

    def on_button_click(self, button):
        # Handle button clicks
        if button == '=':
            self.calculate()
        elif button == 'Delete':
            self.delete_char()
        elif button == 'AC':
            self.all_clear()
        else:
            self.expression += str(button)
            self.input_text.set(self.expression)

    def delete_char(self):
        # Function to delete the last character from expression
        if self.expression:
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)

    def all_clear(self):
        # Function to clear the entire expression
        self.expression = ""
        self.input_text.set("")

    def calculate(self):
        # Function to evaluate and display the result
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
