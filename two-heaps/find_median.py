from heapq import heappop, heappush


class MedianFinder:
    minHeap = []
    maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
        return -self.maxHeap[0] / 1.0


def test():
    medianFinder = MedianFinder()
    medianFinder.addNum(3)
    medianFinder.addNum(1)
    print(medianFinder.findMedian())
    medianFinder.addNum(5)
    print(medianFinder.findMedian())
    medianFinder.addNum(4)
    print(medianFinder.findMedian())


test()

# Important note:
# Python's heapq module provides a min-heap by default, which means that the smallest element is at the root.
# To simulate a max-heap (where the largest element is at the root), the code negates the numbers before pushing them into the heap.
# Thus, by pushing -num into maxHeap, it effectively turns the min-heap into a max-heap in terms of the original values.
