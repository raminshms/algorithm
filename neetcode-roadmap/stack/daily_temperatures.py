def dailyTemperatures(temperatures):
    stack = []  # pair of index, temp
    res = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][1]:
            idx, temp = stack.pop()
            res[idx] = i - idx
        stack.append([i, t])

    return res


print(dailyTemperatures([30, 38, 30, 36, 35, 40, 28]))
print(dailyTemperatures([22, 21, 20]))
