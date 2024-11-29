import tkinter as tk

# Function to update the expression in the Entry widget
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

# Function to evaluate the expression
def evaluate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the Entry widget.....
def clear():
    entry.delete(0, tk.END)

# Creating the main window
root = tk.Tk()
root.title("Simple Calculator")

# Creating an Entry widget to display the expression
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define the button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Adding buttons to the grid
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=evaluate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col)

# Creating a Clear button
clear_button = tk.Button(root, text="C", width=5, height=2, font=('Arial', 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Running the main event loop
root.mainloop()
