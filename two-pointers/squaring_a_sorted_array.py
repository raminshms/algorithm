def makeSquares(sortedArr):
    n = len(sortedArr)
    squares = [0 for i in range(n)]
    l = 0
    r = n - 1
    index = n - 1
    while l < r:
        leftSquare = sortedArr[l] * sortedArr[l]
        rightSquare = sortedArr[r] * sortedArr[r]

        if rightSquare >= leftSquare:
            squares[index] = rightSquare
            r -= 1
        else:
            squares[index] = leftSquare
            l += 1

        index -= 1

    return squares


print(makeSquares([-2, -1, 0, 2, 3]))
print(makeSquares([-3, -1, 0, 1, 2]))
