import sys
sys.path.append('C:/Users/Oliwer/Desktop/Magisterka/python FST on pionter machine')
import mroczkowski_library_6 as mo6
import os, random, time
from colorama import Fore
os.system("cls")
print(Fore.BLUE)
from colorama import init, Fore, Style
init()
print(f"{Style.BRIGHT}{Fore.CYAN}")

root = None
for i in range (1,1000):
    n=random.randint(-10000,10000)
    while(n==0):
        n=random.randint(1,10000)
    root = mo6.insert(root,n)

start_time = time.time()
mo6.FST(root, "txt_input")
end_time = time.time()
FST_time = end_time - start_time

with open('time.txt', 'a') as file:
    file.write(f"FST_6:\t{FST_time}\tdivide finger search, list\n")