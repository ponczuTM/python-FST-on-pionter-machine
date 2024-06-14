import os, sys
import subprocess
sys.path.append(os.getcwd())
from colorama import init, Fore, Style

if os.path.exists("memory.txt"):
    os.remove("memory.txt")

test_files = [f"test_memory_{i}.py" for i in range(1, 6)]

for test_file in test_files:
    if not os.path.isfile(test_file):
        print(f"file {test_file} not exists.")
        continue
    
    try:
        subprocess.run(["python", test_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"error in {test_file}: {e}")

os.system("cls")
init()
print(f"{Style.BRIGHT}{Fore.CYAN}")

print("A binary tree has 1000 nodes.")
print("Every node is a number between -10000 and 10000.")
print("Every number that equals 0 was replaced by another.")
print("Every algorithm searched in this tree for 200 numbers.")
print("They used some memory to perform these operations.")
print("result are in file memory.txt")
