import math


def smallestSubarray(nums, s):
    k = math.inf
    windowSum = 0
    start = 0

    for end in range(len(nums)):
        windowSum += nums[end]

        while windowSum >= s:
            k = min(k, end - start + 1)
            windowSum -= nums[start]
            start += 1

    return k if math.isfinite(k) else 0


print(smallestSubarray([2, 1, 5, 2, 3, 2], 7))
print(smallestSubarray([2, 1, 5, 2, 8], 7))
print(smallestSubarray([3, 4, 1, 1, 6], 8))
