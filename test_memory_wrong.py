import mroczkowski_library as mo
import random
import os
import tracemalloc
from colorama import Fore
from colorama import init, Fore, Style

init()
print(f"{Style.BRIGHT}{Fore.CYAN}")

results = []
root = None
for i in range (1,1000):
    n=random.randint(-10000,10000)
    while(n==0):
        n=random.randint(1,10000)
    root = mo.insert(root,n)

def perform_operation(choice, root):
    tracemalloc.start()
    if choice == "1" or choice == "F" or choice == "FST":
        mo.FST(root, "txt_input")
    elif choice == "2" or choice == "B" or choice == "BST":
        mo.BST(root, "txt_input")
    elif choice == "3" or choice == "D" or choice == "DFS":
        mo.DFS(root, "txt_input")
    else:
        print("wrong choice. Try again")
    c, p = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    results.append(c)
    results.append(p)

perform_operation("1", root)
fst_c = results[0]
fst_p = results[1]
results.clear()
perform_operation("2", root)
bst_c = results[0]
bst_p = results[1]
results.clear()
perform_operation("3", root)
dfs_c = results[0]
dfs_p = results[1]
results.clear()
os.system("cls")
depth=mo.find_tree_depth(root)
print(f"A binary tree has 1000 nodes, and the tree's depth is {depth}.")
print("Every node is a number between -1000000 and 1000000.")
print("Every number that equals 0 was replaced by another.")
print("\nEvery algorithm searched in this tree for 200 numbers.")
print("They used some memory to perform these operations.")
print("Here are the results:")
print(f"FST: {fst_c}, peak: {fst_p}")
print(f"BST: {bst_c}, peak: {bst_p}")
print(f"DFS: {dfs_c}, peak: {dfs_p}")