import random
import time
import numpy as np
import os
from colorama import Fore
print(Fore.BLUE)
from colorama import init, Fore, Style
init()
print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}")
os.system("cls")


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    new_node = Node(key)
    if root is None:
        return new_node
    current = root
    while True:
        if key < current.key:
            if current.left is None:
                current.left = new_node
                break
            else:
                current = current.left
        else:
            if current.right is None:
                current.right = new_node
                break
            else:
                current = current.right

    return root

def bst_search(root, target, closest_value=float('inf')):
    while root is not None:
        if abs(target - root.key) < abs(target - closest_value):
            closest_value = root.key
        if target < root.key:
            root = root.left
        elif target > root.key:
            root = root.right
        else:
            return root.key
    return closest_value

def standard_search(arr, target):
    closest_value = arr[0]
    min_difference = abs(target - arr[0])
    for value in arr:
        difference = abs(target - value)
        if difference < min_difference:
            min_difference = difference
            closest_value = value
    return closest_value

def binary_search(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    closest_value = None
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        if closest_value is None or abs(target - arr[mid]) < abs(target - closest_value):
            closest_value = arr[mid]
    return closest_value

def threshold_search(arr, target, threshold):
    closest_value = None
    min_difference = float('inf')
    for value in arr:
        difference = abs(value - target)
        if difference <= threshold and difference < min_difference:
            closest_value = value
            min_difference = difference
    if closest_value is not None:
        return closest_value
    else:
        return arr[0]


def linear_search(arr, target):
    closest_value = arr[0]
    min_difference = abs(target - arr[0])
    for value in arr[1:]:
        difference = abs(target - value)
        if difference < min_difference:
            min_difference = difference
            closest_value = value
    return closest_value


def min_key_linear_search(arr, target):
    closest_value = min(arr, key=lambda x: abs(target - x))
    return closest_value

def numpy_search(arr, target):
    closest_value = np.argmin(np.abs(np.array(arr) - target))
    return arr[closest_value]


def divide_search(arr, target, parts):
    sorted_arr = sorted(arr)
    part_length = len(sorted_arr) // parts
    for i in range(parts):
        start_index = i * part_length
        end_index = (i + 1) * part_length if i < parts - 1 else len(sorted_arr)
        if sorted_arr[start_index] <= target <= sorted_arr[end_index - 1]:
            closest_value = min(sorted_arr[start_index:end_index], key=lambda x: abs(x - target))
            return closest_value
    return None



array = [random.randint(-1000000, 1000000) for _ in range(1000000)]
threshold = int(len(array)/10)
parts = int(len(array)/10)
target_value = 0

start_time = time.time()
bst_root = None
for value in array:
    bst_root = insert(bst_root, value)
end_time = time.time()
print(f"tworzenie drzewa: {end_time - start_time}")
    
start_time = time.time()
result_bst = bst_search(bst_root, target_value)
end_time = time.time()
bst_time = end_time - start_time
start_time = time.time()
result_standard = standard_search(array, target_value)
end_time = time.time()
standard = end_time - start_time
start_time = time.time()
result_threshold = threshold_search(array, target_value, threshold)
end_time = time.time()
tresh = end_time - start_time
start_time = time.time()
result_linear = linear_search(array, target_value)
end_time = time.time()
line = end_time - start_time
start_time = time.time()
result_min_key_linear = min_key_linear_search(array, target_value)
end_time = time.time()
mkline = end_time - start_time
start_time = time.time()
result_binary = binary_search(array, target_value)
end_time = time.time()
binary = end_time - start_time
start_time = time.time()
result_numpy = numpy_search(array, target_value)
end_time = time.time()
numpy_time = end_time - start_time
start_time = time.time()
result_divide = divide_search(array, target_value, parts)
end_time = time.time()
divide_time = end_time - start_time


print(f"Przeszukiwanie standardowe:\tliczba: {result_standard}, Czas: {standard} sekundy")
print(f"Przeszukiwanie z tresholdem:\tliczba: {result_threshold}, Czas: {tresh} sekundy")
print(f"Przeszukiwanie liniowe:\t\tliczba: {result_linear}, Czas: {line} sekundy")
print(f"przeszukiwanie m-k liniowe:\tliczba: {result_min_key_linear}, Czas: {mkline} sekundy")
print(f"Przeszukiwanie binarne:\t\tliczba: {result_binary}, Czas: {binary} sekundy")
print(f"Przeszukiwanie dzielone:\tliczba: {result_divide}, Czas: {divide_time}")
print(f"Przeszukiwanie numpy:\t\tliczba: {result_numpy}, Czas: {numpy_time} sekundy")
print(f"Przeszukiwanie BST:\t\tliczba: {result_bst}, Czas: {bst_time} sekundy")