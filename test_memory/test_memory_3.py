import sys
sys.path.append('C:/Users/Oliwer/Desktop/Magisterka/python FST on pionter machine')
import mroczkowski_library_2 as mo3
import random
import psutil
from colorama import init, Fore, Style

init()
print(f"{Style.BRIGHT}{Fore.CYAN}")

root = None
for i in range (1,1000):
    n=random.randint(-1000,1000)
    while(n==0):
        n=random.randint(1,1000)
    root = mo3.insert(root,n)

def measure_memory_usage(algorithm):
    process = psutil.Process()
    before_memory = process.memory_info().rss
    algorithm()
    after_memory = process.memory_info().rss
    memory_used = after_memory - before_memory
    return memory_used / (1024 * 1024)

memory_used_fst = measure_memory_usage(lambda: mo3.FST(root, "txt_input"))
with open('memory.txt', 'a') as file:
    file.write(f"FST_3:\t{memory_used_fst:.4f} MB\ttreshold finger search, set()\n")