import random
import time

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
    for value in arr:
        if closest_value is None or abs(target - value) < abs(target - closest_value):
            closest_value = value
    return closest_value

array = [random.randint(-1000000, 1000000) for _ in range(10000000)]
target_value = -9929

start_time = time.time()
result_standard = standard_search(array, target_value)
end_time = time.time()
print(f"Standardowe przeszukanie: {result_standard}, Czas: {end_time - start_time} sekundy")
start_time = time.time()
result_binary = binary_search(array, target_value)
end_time = time.time()
print(f"Przeszukiwanie binarne: {result_binary}, Czas: {end_time - start_time} sekundy")
threshold = 1000
start_time = time.time()
result_threshold = threshold_search(array, target_value, threshold)
end_time = time.time()
print(f"Przeszukiwanie z tresholdem: {result_threshold}, Czas: {end_time - start_time} sekundy")