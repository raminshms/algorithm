def carFleet(target, position, speed):
    pairs = [[position[i], speed[i]] for i in range(len(position))]

    pairs.sort(reverse=True)

    stack = []
    for p, s in pairs:
        t = (target - p) / s
        stack.append(t)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


def carFleet2(target, position, speed):
    n = len(position)
    pairs = [[position[i], speed[i]] for i in range(n)]

    pairs.sort(reverse=True)

    res = prev = 0
    for p, s in pairs:
        t = (target - p) / s

        if prev < t:
            res += 1
            prev = t

    return res


print(carFleet2(10, [1, 4],  [3, 2]))
print(carFleet2(10, [4, 1, 0, 7],  [2, 2, 1, 1]))
print(carFleet2(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
print(carFleet2(10, [3], [3]))
print(carFleet2(100, [0, 2, 4], [4, 2, 1]))
