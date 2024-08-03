from heapq import heappop, heappush


def findKthSmallestNumber(arr, k):
    maxHeap = []

    for i in range(k):
        heappush(maxHeap, -arr[i])

    for i in range(k, len(arr)):
        if arr[i] < -maxHeap[0]:
            heappop(maxHeap)
            heappush(maxHeap, -arr[i])

    return - maxHeap[0]


print(findKthSmallestNumber([1, 5, 12, 2, 11, 5], 3))
print(findKthSmallestNumber([1, 5, 12, 2, 11, 5], 4))
print(findKthSmallestNumber([5, 12, 11, -1, 12], 3))
