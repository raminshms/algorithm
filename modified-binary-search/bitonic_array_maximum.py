def findMaxInBitonicArray(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        m = (start + end) // 2

        if arr[m] > arr[m+1]:
            end = m
        else:
            start = m + 1

    return arr[start]


print(findMaxInBitonicArray([1, 3, 8, 12, 4, 2]))
print(findMaxInBitonicArray([3, 8, 3, 1]))
print(findMaxInBitonicArray([1, 3, 8, 12]))
print(findMaxInBitonicArray([10, 9, 8]))
