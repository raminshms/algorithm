def maximumSubarraySum(nums, k):
    maxSum = 0
    left = 0
    windowSum = 0

    for right in range(len(nums)):
        windowSum += nums[right]

        if right >= k - 1:
            maxSum = max(maxSum, windowSum)
            windowSum -= nums[left]
            left += 1

    return maxSum


print(maximumSubarraySum([2, 1, 5, 1, 3, 2], 3))
print(maximumSubarraySum([2, 3, 4, 1, 5], 2))
