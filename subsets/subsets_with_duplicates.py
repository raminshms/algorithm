def findSubsetsWithDuplicates(nums):
    subsets = []
    subsets.append([])
    nums.sort()

    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex + 1
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex + 1):
            set = list(subsets[j])
            set.append(nums[i])
            subsets.append(set)
    return subsets


print(findSubsetsWithDuplicates([1, 3, 3]))
print(findSubsetsWithDuplicates([1, 5, 3, 3]))
