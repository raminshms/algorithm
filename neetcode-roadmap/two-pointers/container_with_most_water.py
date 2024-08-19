def maxArea(height):
    l = 0
    r = len(height) - 1
    mostWater = 0
    while l < r:
        h = min(height[l], height[r])
        width = r - l
        mostWater = max(mostWater, h*width)

        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1

    return mostWater


print(maxArea([1, 7, 2, 5, 4, 7, 3, 6]))
print(maxArea([2, 2, 2]))
print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 1]))
