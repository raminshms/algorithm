import math


def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    res = 1

    while l <= r:
        k = (l + r) // 2

        time = 0
        for p in piles:
            time += math.ceil(p/k)

        if time > h:
            l = k + 1
        else:
            res = k
            r = k - 1
    return res


print(minEatingSpeed(piles=[3, 6, 7, 11], h=8))
print(minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
print(minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
print(minEatingSpeed(piles=[312884470], h=312884469))
