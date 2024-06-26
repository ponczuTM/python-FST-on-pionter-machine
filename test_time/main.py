import os
import subprocess

if os.path.exists("time.txt"):
    os.remove("time.txt")

test_files = [f"test_time_{i}.py" for i in range(1, 7)]

for test_file in test_files:
    subprocess.run(["python", test_file], check=True)

os.system("cls")
print("A binary tree has 1000 nodes.")
print("Every node is a number between -10000 and 10000.")
print("Every number that equals 0 was replaced by another.")
print("Every algorithm searched in this tree for 200 numbers.")
print("They needed some time to perform these operations.")
print("result are in file time.txt")