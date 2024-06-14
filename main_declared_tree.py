import mroczkowski_library as mo
#mo.help()
import os
from colorama import Fore
os.system("cls")
print(Fore.BLUE)

from colorama import init, Fore, Style
init()
print(f"{Style.BRIGHT}{Fore.CYAN}")

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

choice = input("which algorithm do you choose?:\nFST: 1 / F / FST\nBST: 2 / B / BST\nDFS: 3 / D / DFS\n").upper()
if choice == "1" or choice == "F" or choice == "FST":
    mo.FST(root)
elif choice == "2" or choice == "B" or choice == "BST":
    mo.BST(root)
elif choice == "3" or choice == "D" or choice == "DFS":
    mo.DFS(root)
else:
    print("wrong choice. Try again")
print("--------------------")
