def findMissingNumber(nums):
    i = 0
    n = len(nums)
    while i < n:
        correctIndex = nums[i]

        if correctIndex < n and correctIndex != i:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    return n


print(findMissingNumber([4, 0, 3, 1]))
print(findMissingNumber([8, 3, 5, 2, 4, 6, 0, 1]))
