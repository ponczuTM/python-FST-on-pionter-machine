import random
import time

array1 = [random.randint(-100000000, 100000000) for _ in range(10000000)]
array2 = array1.copy()

start_time = time.time()
array1.sort()
end_time = time.time()
sort = end_time - start_time
start_time = time.time()
array2 = sorted(array2)
end_time = time.time()
sorted = end_time - start_time

print(f'{sort}is time for 100000000 array for sort()')
print(f'{sorted}is time for 100000000 array for sorted()')