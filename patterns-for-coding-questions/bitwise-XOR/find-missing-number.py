def findMissingNumber(nums):
    n = len(nums) + 1

    x1 = 1
    for i in range(2, n + 1):
        x1 = x1 ^ i

    x2 = nums[0]
    for i in range(1, len(nums)):
        x2 = x2 ^ nums[i]

    return x1 ^ x2


print(findMissingNumber([1, 5, 2, 6, 4]))
