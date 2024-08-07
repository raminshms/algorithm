from heapq import heappop, heappush


def topKFrequent(nums, k):
    counter = {}

    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    maxHeap = []
    for n in counter:
        heappush(maxHeap, [-counter[n], n])

    res = []
    for _ in range(k):
        _, num = heappop(maxHeap)
        res.append(num)

    return res


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1], 1))
