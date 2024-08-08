def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for n in nums:
        lenght = 0
        if n - 1 not in numSet:
            lenght = 1
            while n + lenght in numSet:
                lenght += 1
            longest = max(longest, lenght)

    return longest


print(longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
print(longestConsecutive([0]))
print(longestConsecutive([0, 0]))
print(longestConsecutive([2, 20, 4, 10, 3, 4, 5]))
print(longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1]))
print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
