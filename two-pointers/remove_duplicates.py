def removeDuplicates(sortedArr):
    nextNonDuplicateIndex = 1

    for i in range(1, len(sortedArr)):
        if sortedArr[nextNonDuplicateIndex - 1] != sortedArr[i]:
            sortedArr[nextNonDuplicateIndex] = sortedArr[i]
            nextNonDuplicateIndex += 1

    return nextNonDuplicateIndex


print(removeDuplicates([2, 3, 3, 3, 6, 9, 9]))
print(removeDuplicates([2, 2, 2, 11]))
