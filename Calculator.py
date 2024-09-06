import tkinter as tk

def update_screen(value):
    if screen.get() == "0" or screen.get() == "Error!":
        screen.set(value)
    else:
        screen.set(screen.get() + value)

def calculate():
    try:
        result = eval(screen.get())
        if isinstance(result, (int, float)):
            screen.set(result)
        else:
            screen.set("Error!")
    except:
        screen.set("Error!")

def clear():
    screen.set("0")

def delete():
    current_text = screen.get()
    if len(current_text) > 1:
        screen.set(current_text[:-1])
    else:
        screen.set("0")

apl  = tk.Tk()
apl .title("Calculator")

screen = tk.StringVar(value="0")
screen_display = tk.Entry(apl, textvariable=screen, font=("monospace", 30), bd=10, relief="ridge", justify="right")
screen_display.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', '←'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(apl, text=button, command=calculate, font=("Arial", 20), width=5, height=2).grid(row=row_val, column=col_val, columnspan=2, sticky="nsew")
        col_val += 2
    elif button == 'C':
        tk.Button(apl, text=button, command=clear, font=("Arial", 20), width=5, height=2).grid(row=row_val, column=col_val, sticky="nsew")
        col_val += 1
    elif button == '←':
        tk.Button(apl, text=button, command=delete, font=("Arial", 20), width=5, height=2).grid(row=row_val, column=col_val, sticky="nsew")
        col_val += 1
    else:
        tk.Button(apl, text=button, command=lambda b=button: update_screen(b), font=("Arial", 20), width=5, height=2).grid(row=row_val, column=col_val, sticky="nsew")
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

for i in range(4):
    apl.grid_columnconfigure(i, weight=1)
for i in range(5):
    apl.grid_rowconfigure(i, weight=1)


apl.mainloop()
