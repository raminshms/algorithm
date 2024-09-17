def intersection(nums1, nums2):
    hashMap = {}

    for n in nums1:
        hashMap[n] = 1

    res = []
    for n in nums2:
        if n in hashMap:
            res.append(n)
            del hashMap[n]

    return res


print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
