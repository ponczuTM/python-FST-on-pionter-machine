import os, sys
import subprocess
sys.path.append('C:/Users/Oliwer/Desktop/Magisterka/python FST on pionter machine')
import mroczkowski_library as mo
from colorama import init, Fore, Style

if os.path.exists("memory.txt"):
    os.remove("memory.txt")
else:
    print("Plik memory.txt nie istnieje, kontynuuję.")

test_files = [f"test_memory_{i}.py" for i in range(1, 6)]

# Uruchamianie plików jeden po drugim
for test_file in test_files:
    # Sprawdzenie, czy plik istnieje przed próbą jego uruchomienia
    if not os.path.isfile(test_file):
        print(f"Plik {test_file} nie istnieje.")
        continue
    
    try:
        # Uruchomienie pliku Pythona
        subprocess.run(["python", test_file], check=True)
        print(f"Uruchomiono plik {test_file}")
    except subprocess.CalledProcessError as e:
        print(f"Błąd podczas uruchamiania pliku {test_file}: {e}")

os.system("cls")
init()
print(f"{Style.BRIGHT}{Fore.CYAN}")

print("A binary tree has 1000 nodes.")
print("Every node is a number between -1000 and 1000.")
print("Every number that equals 0 was replaced by another.")
print("Every algorithm searched in this tree for 200 numbers.")
print("They used some memory to perform these operations.")
print("result are in file memory.txt")
