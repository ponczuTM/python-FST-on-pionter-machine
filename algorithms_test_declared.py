import mroczkowski_library as mo
import os
import random
os.system("cls")

n = int(input("enter the depth of the binary tree: "))
depth = (2 ** n) - 1
root = None
print(depth)
with open("depth.txt", "w") as file:
    file.write(str(depth))

print("---------------")
print("---------------")
print("---------------")
for _ in range(depth):
    p = random.randint(1, 101)
    root = mo.insert(root, p)

choice = input("which algorithm do you choose?:\nFST: 1 / F / FST\nBST: 2 / B / BST\nDFS: 3 / D / DFS\n").upper()
if choice == "1" or choice == "F" or choice == "FST":
    mo.FST(root)
elif choice == "2" or choice == "B" or choice == "BST":
    mo.BST(root)
elif choice == "3" or choice == "D" or choice == "DFS":
    mo.DFS(root)
else:
    print("wrong choice. Try again")