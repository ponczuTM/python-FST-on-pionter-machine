import mroczkowski_library as mo
import os
os.system("cls")

values = [260, 36, 118, -284, 933, -684, -565, -387, 281, -14, 428, -331, 959, -702, 884, -951, 727, 467, -107, 251, 212, -83, 923, 925, -948, 917, -644, 31, 493, 362, 872, 64, -524, -592, 24, 996, 647, -929, -528, 707, 798, -353, 47, 573, -892, -421, 426, 584, -166, 370, 379, -423, 525, 580, -58, 361, -469, 500, -629, 581, -298, 738, -431, 304, 789, 117, -137, -492, 810, 377, 629, -853, -688, 129, -891, -462, 295, -838, -483, -232, -250, 139, -653, 676, -552, -671, 964, 630, -844, -832, 557, -354, -163, -819, 113, 196, 984, -703, -865, 153]
root = None
for value in values:
    root = mo.insert(root, value)

choice = input("which algorithm do you choose?:\nFST: 1 / F / FST\nBST: 2 / B / BST\nDFS: 3 / D / DFS\n").upper()
if choice == "1" or choice == "F" or choice == "FST":
    mo.FST(root)
elif choice == "2" or choice == "B" or choice == "BST":
    mo.BST(root)
elif choice == "3" or choice == "D" or choice == "DFS":
    mo.DFS(root)
else:
    print("wrong choice. Try again")
print("--------------------")
