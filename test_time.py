import mroczkowski_library as mo
import mroczkowski_library_2 as mo2
import mroczkowski_library_3 as mo3
import mroczkowski_library_4 as mo4
import mroczkowski_library_5 as mo5
import mroczkowski_library_6 as mo6
import random, time, os
from colorama import init, Fore, Style
init()
print(f"{Style.BRIGHT}{Fore.CYAN}")

results = []
root = None
root2 = None
root3 = None
root4 = None
root5 = None
root6 = None
for i in range (1,1000):
    n=random.randint(-10000,10000)
    while(n==0):
        n=random.randint(1,10000)
    root = mo.insert(root,n)

start_time = time.time()
mo.FST(root, "txt_input")
end_time = time.time()
FST_time = end_time - start_time

start_time = time.time()
mo2.FST(root, "txt_input")
end_time = time.time()
FST_time2 = end_time - start_time

start_time = time.time()
mo3.FST(root, "txt_input")
end_time = time.time()
FST_time3 = end_time - start_time

start_time = time.time()
mo4.FST(root, "txt_input")
end_time = time.time()
FST_time4 = end_time - start_time

start_time = time.time()
mo5.FST(root, "txt_input")
end_time = time.time()
FST_time5 = end_time - start_time

start_time = time.time()
mo6.FST(root, "txt_input")
end_time = time.time()
FST_time6 = end_time - start_time

start_time = time.time()
mo.BST(root, "txt_input")
end_time = time.time()
BST_time = end_time - start_time

start_time = time.time()
mo.DFS(root, "txt_input")
end_time = time.time()
DFS_time = end_time - start_time

os.system("cls")
print(f"FST: {FST_time}")
print(f"FST_2: {FST_time2}")
print(f"FST_3: {FST_time3}")
print(f"FST_4: {FST_time4}")
print(f"FST_5: {FST_time5}")
print(f"FST_6: {FST_time6}")
print(f"BST: {BST_time}")
print(f"DFS: {DFS_time}")