def containsDuplicate(nums):
    numsHashMap = {}

    for num in nums:
        if num in numsHashMap:
            return True
        else:
            numsHashMap[num] = 1

    return False


print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
