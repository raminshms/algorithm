from typing import List


def insertInterval(intervals: List[List[int]], newInterval: List[int]):
    start = 0
    insertIndex = 0
    for i in range(len(intervals)):
        start = max(intervals[i][0], start)
        if newInterval[0] >= start:
            insertIndex = i + 1

    intervals.insert(insertIndex, newInterval)

    return mergeIntervals(intervals)


def mergeIntervals(intervals: List[List[int]]):
    n = len(intervals)

    if n < 2:
        return intervals

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


print(insertInterval([[1, 3], [5, 7], [8, 12]], [4, 6]))
print(insertInterval([[1, 3], [5, 7], [8, 12]], [4, 10]))
print(insertInterval([[2, 3], [5, 7]], [1, 4]))
