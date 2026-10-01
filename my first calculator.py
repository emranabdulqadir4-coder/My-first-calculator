import tkinter as tk

# 1. Set up the main application window
root = tk.Tk()
root.title("My first Calculator")
root.geometry("500x600")
root.configure(bg="black")

# 2. Create the display screen
screen = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right", bg="#1e1e1e", fg="white", insertbackground="white")
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# 3. Define button click actions (Connecting the logic)
def button_click(number):
    current = screen.get()
    screen.delete(0, tk.END)
    screen.insert(0, current + str(number))

def clear_screen():
    screen.delete(0, tk.END)

def calculate_result():
    try:
        # eval() parses and calculates the entire string expression automatically!
        result = eval(screen.get())
        screen.delete(0, tk.END)
        screen.insert(0, str(result))
    except Exception:
        screen.delete(0, tk.END)
        screen.insert(0, "Error")

# 4. Create and grid the layout buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        action = calculate_result
    elif text == 'C':
        action = clear_screen
    else:
        action = lambda x=text: button_click(x)
        
    btn = tk.Button(root, text=text, font=("Arial", 14), command=action)
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Configure rows and columns to resize smoothly
for i in range(5):
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

root.mainloop()
