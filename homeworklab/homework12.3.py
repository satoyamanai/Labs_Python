def is_subsequence(a, b):
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            j += 1
        i += 1

    return j == len(b)


# example
a = [3, 5, 8, 10, 12, 15]
b = [5, 10, 15]
result = is_subsequence(a, b)
print(result)