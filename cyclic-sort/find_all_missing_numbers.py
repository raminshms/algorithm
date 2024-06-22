def findAllMissingNumbers(nums):
    i, n = 0, len(nums)

    while i < n:
        correctIndex = nums[i] - 1

        if correctIndex != i and correctIndex < n and nums[i] != nums[correctIndex]:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1

    missingNumbers = []
    for i in range(n):
        if i+1 != nums[i]:
            missingNumbers.append(i+1)

    return missingNumbers


print(findAllMissingNumbers([2, 3, 1, 8, 2, 3, 5, 1]))
print(findAllMissingNumbers([2, 4, 1, 2]))
print(findAllMissingNumbers([2, 3, 2, 1]))
