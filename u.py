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
