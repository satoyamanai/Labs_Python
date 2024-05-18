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