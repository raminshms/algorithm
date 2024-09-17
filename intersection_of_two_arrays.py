def intersection(nums1, nums2):
    numsMap = {}
    isArr1Bigger = len(nums1) >= len(nums2)

    for n in nums1 if isArr1Bigger else nums2:
        numsMap[n] = 1

    res = []
    for n in nums2 if isArr1Bigger else nums1:
        if n in numsMap:
            del numsMap[n]
            res.append(n)

    return res


print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
