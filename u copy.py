import mroczkowski_library as mo
import random
import time
[...]
for i in range (1,1000):
    n=random.randint(-10000,10000)
    while(n==0):
        n=random.randint(1,10000)
    root = mo.insert(root,n)

start_time = time.time()
mo.FST(root, "txt_input")
end_time = time.time()
FST_time = end_time - start_time
[...]
print(f"FST: {FST_time}")
[...]
