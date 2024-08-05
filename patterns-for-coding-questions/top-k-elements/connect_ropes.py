from heapq import heappop, heappush


def findConnectRopes(arr):
    minHeap = []

    for num in arr:
        heappush(minHeap, num)

    result, tmp = 0, 0

    while len(minHeap) > 1:
        tmp = heappop(minHeap) + heappop(minHeap)
        result += tmp
        heappush(minHeap, tmp)

    return result


print(findConnectRopes([1, 3, 11, 5]))
print(findConnectRopes([3, 4, 5, 6]))
print(findConnectRopes([1, 3, 11, 5, 2]))
