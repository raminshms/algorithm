from heapq import heappop, heappush


def findTopNumbers(arr, k):
    n = len(arr)
    minHeap = []

    for i in range(k):
        heappush(minHeap, arr[i])

    for i in range(k, n):
        if arr[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, arr[i])

    return minHeap


print(findTopNumbers([3, 1, 5, 12, 2, 11], 3))
print(findTopNumbers([5, 12, 11, -1, 12], 3))
