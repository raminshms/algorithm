def cyclicSort(nums):
    i = 0
    while i < len(nums):
        currentNum = nums[i]
        correctIndex = currentNum - 1

        if correctIndex != i:
            nums[i], nums[correctIndex],  = nums[correctIndex], nums[i]
        else:
            i += 1

    return nums


print(cyclicSort([3, 1, 5, 4, 2]))
print(cyclicSort([2, 6, 4, 3, 1, 5]))
print(cyclicSort([1, 5, 6, 4, 3, 2]))