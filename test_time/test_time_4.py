import sys
sys.path.append('C:/Users/Oliwer/Desktop/Magisterka/python FST on pionter machine')
import mroczkowski_library_4 as mo4
import random, time
from colorama import init, Fore, Style
print(Fore.BLUE)
init()
print(f"{Style.BRIGHT}{Fore.CYAN}")

root = None
for i in range (1,1000):
    n=random.randint(-1000,1000)
    while(n==0):
        n=random.randint(1,1000)
    root = mo4.insert(root,n)

start_time = time.time()
mo4.FST(root, "txt_input")
end_time = time.time()
FST_time = end_time - start_time

with open('time.txt', 'a') as file:
    file.write(f"FST_4: {FST_time}\n")