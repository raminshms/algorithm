def twoSum(nums, target):
    hm = {}

    for index, num in enumerate(nums):
        tmp = target - num
        if tmp in hm:
            return [hm[tmp], index]
        else:
            hm[num] = index

    return [-1, -1]


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
