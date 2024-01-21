import tkinter as tk
from tkinter import font
import mroczkowski_library as mo

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
    with open('input_gui.txt', 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')
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

def search_numbers():
    mo.FST(root, "txt_input")
    with open("found_numbers.txt", "r") as file:
        found_numbers = set(map(int, file.read().split(',')))

    for number in numbers:
        if number in found_numbers:
            buttons[number]["bg"] = "green"
        else:
            buttons[number]["bg"] = "red"

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
search_button = tk.Button(r, text="Search Numbers", command=search_numbers, width=15)
search_button.pack()
r.mainloop()
