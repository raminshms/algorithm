from typing import List


def mergeIntervals(intervals: List[List[int]]):
    n = len(intervals)

    if n < 2:
        return intervals

    # intervals[i] = [starti, endi]
    intervals.sort(key=lambda interval: interval[0])

    start = intervals[0][0]
    end = intervals[0][1]

    mergedIntervals = []
    for i in range(1, n):
        currentInterval = intervals[i]

        if currentInterval[0] <= end:
            end = max(end, currentInterval[1])
        else:
            mergedIntervals.append([start, end])
            start = currentInterval[0]
            end = currentInterval[1]

    mergedIntervals.append([start, end])
    return mergedIntervals


print(mergeIntervals([[1, 4], [2, 5], [7, 9]]))
print(mergeIntervals([[6, 7], [2, 4], [5, 9]]))
print(mergeIntervals([[1, 4], [2, 6], [3, 5]]))
print(mergeIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(mergeIntervals([[1, 4], [4, 5]]))
