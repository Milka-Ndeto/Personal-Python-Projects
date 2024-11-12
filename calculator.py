import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = str(eval(entry.get()))  # Use eval to calculate the result
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(0, result)  # Insert the result
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to add button press to entry field
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Create main window
window = tk.Tk()
window.title("Calculator")

# Create entry field
entry = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and place buttons on the window
for (text, row, col) in buttons:
    button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: button_click(t) if t != '=' else evaluate_expression())
    button.grid(row=row, column=col)

# Add clear button
clear_button = tk.Button(window, text="C", width=5, height=2, font=("Arial", 18), command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=2)

# Start the Tkinter event loop
window.mainloop()
