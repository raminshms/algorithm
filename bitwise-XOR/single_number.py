def findSingleNumber(arr):
    x = 0
    for num in arr:
        x = num ^ x
    return x


print(findSingleNumber([1, 4, 2, 1, 3, 2, 3]))
print(findSingleNumber([7, 9, 7]))
