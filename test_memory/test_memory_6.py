import sys
sys.path.append('C:/Users/Oliwer/Desktop/Magisterka/python FST on pionter machine')
import mroczkowski_library_6 as mo6
import random
import psutil
from colorama import init, Fore, Style

init()
print(f"{Style.BRIGHT}{Fore.CYAN}")

root = None
for i in range (1,1000):
    n=random.randint(-10000,10000)
    while(n==0):
        n=random.randint(1,10000)
    root = mo6.insert(root,n)

def measure_memory_usage(algorithm):
    process = psutil.Process()
    before_memory = process.memory_info().rss
    algorithm()
    after_memory = process.memory_info().rss
    memory_used = after_memory - before_memory
    return memory_used / (1024 * 1024)

memory_used_fst = measure_memory_usage(lambda: mo6.FST(root, "txt_input"))
with open('memory.txt', 'a') as file:
    file.write(f"FST_6:\t{memory_used_fst:.4f} MB\tdivide finger search, list\n")