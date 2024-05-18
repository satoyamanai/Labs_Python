import time
import math

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def golden_section_search(arr, target):
    low = 0
    high = len(arr) - 1
    phi = (math.sqrt(5) - 1) / 2
    while low <= high:
        i = int(low + (high - low) * phi)
        if arr[i] == target:
            return i
        elif arr[i] < target:
            low = i + 1
        else:
            high = i - 1
    return -1

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if arr[low] == target:
            return low
        if arr[high] == target:
            return high
        if low == high:
            return -1
        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        if arr[pos] < target:
            low = pos + 1
        elif arr[pos] > target:
            high = pos - 1
        else:
            return pos
    return -1

def compare_search_methods(arr, target):
    start_time = time.time()
    binary_search_result = binary_search(arr, target)
    binary_search_time = time.time() - start_time

    start_time = time.time()
    golden_section_search_result = golden_section_search(arr, target)
    golden_section_search_time = time.time() - start_time

    start_time = time.time()
    interpolation_search_result = interpolation_search(arr, target)
    interpolation_search_time = time.time() - start_time

    print("Binary Search Result:", binary_search_result)
    print("Binary Search Time:", binary_search_time)
    print("Golden Section Search Result:", golden_section_search_result)
    print("Golden Section Search Time:", golden_section_search_time)
    print("Interpolation Search Result:", interpolation_search_result)
    print("Interpolation Search Time:", interpolation_search_time)

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
compare_search_methods(arr, target)