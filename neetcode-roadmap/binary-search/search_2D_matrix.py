def searchMatrix(matrix, target):
    top = 0
    bot = len(matrix) - 1
    while top <= bot:
        row = (top + bot) // 2

        if matrix[row][-1] < target:
            top = row + 1
        elif matrix[row][0] > target:
            bot = row - 1
        else:
            break

    l = 0
    r = len(matrix[0]) - 1
    while l <= r:
        m = (l + r) // 2

        if matrix[row][m] < target:
            l = m + 1
        elif matrix[row][m] > target:
            r = m - 1
        else:
            return True

    return False


print(searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10))
print(searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15))
print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
