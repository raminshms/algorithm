from heapq import heappush, heappushpop


def kClosest(points, k):
    maxHeap = []

    for i in range(len(points)):
        x, y = points[i]
        d = x ** 2 + y ** 2
        if len(maxHeap) == k:
            heappushpop(maxHeap, [-d, x, y])
        else:
            heappush(maxHeap, [-d, x, y])

    return [[x, y] for _, x, y in maxHeap]


print(kClosest([[1, 2], [1, 3]], 1))
print(kClosest([[1, 3], [3, 4], [2, -1]], 2))
