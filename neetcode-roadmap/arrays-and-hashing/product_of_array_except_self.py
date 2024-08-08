def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n

    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]

    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


print(productExceptSelf([1, 2, 4, 6]))
print(productExceptSelf([-1, 0, 1, 2, 3]))
