def binarySearch(arr, key):
    start = 0
    end = len(arr) - 1
    isAscending = arr[end] >= arr[start]
    while start <= end:
        m = (end + start) // 2
        mid = arr[m]
        if mid == key:
            return m

        if isAscending:
            if mid > key:
                end = m - 1
            elif mid < key:
                start = m + 1
        else:
            if mid > key:
                start = m + 1
            elif mid < key:
                end = m - 1

    return -1


print(binarySearch([4, 6, 10], 10))
print(binarySearch([1, 2, 3, 4, 5, 6, 7], 5))
print(binarySearch([10, 6, 4], 10))
print(binarySearch([10, 6, 4], 4))
