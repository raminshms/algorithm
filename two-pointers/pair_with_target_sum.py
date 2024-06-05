def targetSumPair(sortedArr, targetSum):
    l = 0
    r = len(sortedArr) - 1

    while l < r:
        sum = sortedArr[l] + sortedArr[r]

        if sum == targetSum:
            return [l, r]
        elif sum > targetSum:
            r -= 1
        else:
            l += 1

    return [-1, -1]


print(targetSumPair([1, 2, 3, 4, 6], 6))
print(targetSumPair([2, 5, 9, 11], 11))
