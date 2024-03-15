import sys
sys.path.append('C:/Users/Oliwer/Desktop/Magisterka/python FST on pionter machine')
import mroczkowski_library as mo
import os, random, time
from colorama import Fore
os.system("cls")
print(Fore.BLUE)
from colorama import init, Fore, Style
init()
print(f"{Style.BRIGHT}{Fore.CYAN}Tekst pogrubiony")

root = None
for i in range (1,1000):
    n=random.randint(-1000, 1000)
    while(n==0):
        n=random.randint(1,1000)
    root = mo.insert(root,n)

start_time = time.time()
mo.BST(root, "txt_input")
end_time = time.time()
BST_time = end_time - start_time

start_time = time.time()
mo.DFS(root, "txt_input")
end_time = time.time()
DFS_time = end_time - start_time

start_time = time.time()
mo.FST(root, "txt_input")
end_time = time.time()
FST_time = end_time - start_time

with open('time.txt', 'a') as file:
    file.write(f"FST_1:\t{FST_time}\tstandard finger search\n")
    file.write(f"BST_1:\t{BST_time}\tstandard search\n")
    file.write(f"DFS_1:\t{DFS_time}\tstandard search\n")