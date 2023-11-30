import mroczkowski_library as mo
#mo.help()
import random
import os
from colorama import Fore
os.system("cls")

from colorama import init, Fore, Style
init()
print(f"{Style.BRIGHT}{Fore.CYAN}Tekst pogrubiony")



root = None
for i in range (1,1000):
    root = mo.insert(root, random.randint(1,10000))




g=0
import tracemalloc

def perform_operation(choice, root):
    tracemalloc.start()  # Rozpocznij śledzenie pamięci przed wykonaniem operacji

    if choice == "1" or choice == "F" or choice == "FST":
        mo.FST(root, "txt_input")
    elif choice == "2" or choice == "B" or choice == "BST":
        mo.BST(root, "txt_input")
    elif choice == "3" or choice == "D" or choice == "DFS":
        mo.DFS(root, "txt_input")
    else:
        print("wrong choice. Try again")

    current, peak = tracemalloc.get_traced_memory()
    print(f"\nCurrent memory usage: {current / 10**3}")
    print(f"Peak memory usage: {peak / 10**3}")
    g=peak
    tracemalloc.stop()
    return g

a = perform_operation("1", root)
b = perform_operation("2", root)
c = perform_operation("3", root)

os.system("cls")
print(f"\na: {a} b\nb: {b} b\nc: {c} b")
