import mroczkowski_library_2 as mo
import os
from colorama import Fore
os.system("cls")
print(Fore.BLUE)
import random
import tracemalloc
import time
from colorama import init, Fore, Style
init()
print(f"{Style.BRIGHT}{Fore.CYAN}")

results = []
root = None
for i in range (1,1000):
    n=random.randint(-1000000,1000000)
    while(n==0):
        n=random.randint(1,1000000)
    root = mo.insert(root,n)

start_time = time.time()
mo.FST(root, "txt_input")
end_time = time.time()
FST_time = end_time - start_time

start_time = time.time()
mo.BST(root, "txt_input")
end_time = time.time()
BST_time = end_time - start_time

start_time = time.time()
mo.DFS(root, "txt_input")
end_time = time.time()
DFS_time = end_time - start_time
print(f"FST: {FST_time}")
print(f"BST: {BST_time}")
print(f"DFS: {DFS_time}")