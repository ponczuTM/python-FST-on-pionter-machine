import mroczkowski_library as mo
import tkinter as tk
from tkinter import font
root = None
root = mo.insert(root, 50)
root = mo.insert(root, 25)
root = mo.insert(root, 75)
root = mo.insert(root, 16)
root = mo.insert(root, 37)
root = mo.insert(root, 68)
root = mo.insert(root, 89)
root = mo.insert(root, 96)
root = mo.insert(root, 78)
root = mo.insert(root, 73)
root = mo.insert(root, 53)
root = mo.insert(root, 47)
root = mo.insert(root, 29)
root = mo.insert(root, 22)
root = mo.insert(root, 7)

def handle_button_click(value):
    if value in numbers:
        numbers.remove(value)
        buttons[value]["state"] = tk.NORMAL
        buttons[value]["bg"] = "SystemButtonFace"
    else:
        numbers.append(value)
        buttons[value]["state"] = tk.DISABLED
        buttons[value]["bg"] = "lightblue"

def check_numbers():
    print("Zaznaczone liczby:", numbers)

def exit_app():
    with open('input.txt', 'w') as file:
        numbers_str = ', '.join(map(str, numbers))
        file.write(numbers_str)

    # Perform the search in the binary tree
    with open('input.txt', 'r') as file:
        search_numbers = [int(x) for x in file.read().split(', ')]

    for number in search_numbers:
        found = mo.FST(root, number)  # Perform the search
        if found:
            buttons[number]["bg"] = "green"  # Mark found numbers as green
        else:
            buttons[number]["bg"] = "red"  # Mark not found numbers as red

numbers = []

r = tk.Tk()
r.title("GUI z przyciskami")
frame = tk.Frame(r)
frame.pack()
buttons = {}
for i in range(1, 101):
    if i == 0:
        continue
    row, col = divmod(i - 1, 20)
    row = abs(row)
    buttons[i] = tk.Button(frame, text=str(i), command=lambda i=i: handle_button_click(i), font=font.Font(size=20))
    buttons[i].grid(row=row, column=col)
    buttons[i]["state"] = tk.NORMAL
    buttons[i]["width"] = 3
    buttons[i]["height"] = 1

check_button = tk.Button(r, text="Check", command=check_numbers, width=8)
check_button.pack()
exit_button = tk.Button(r, text="Search", command=exit_app, width=8)
exit_button.pack()
r.mainloop()