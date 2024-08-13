def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        s = numbers[l] + numbers[r]

        if s == target:
            return [l + 1, r + 1]

        if s < target:
            l += 1

        if s > target:
            r -= 1

    return [-1, -1]


print(twoSum([1, 2, 3, 4], 3))
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 3, 4], 6))
print(twoSum([-1, 0], -1))
