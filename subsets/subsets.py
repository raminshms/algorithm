def findSubsets(nums):
    subsets = []

    subsets.append([])

    for num in nums:
        for i in range(len(subsets)):
            currentSet = list(subsets[i])
            currentSet.append(num)
            subsets.append(currentSet)
    return subsets


print(findSubsets([1, 3, 5]))
print(findSubsets([1, 3]))
