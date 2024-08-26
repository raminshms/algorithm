def generateParenthesis(n):
    stack = []
    res = []

    def backtrack(openCount, closeCount):
        if openCount == closeCount == n:
            res.append("".join(stack))
            return

        if openCount < n:
            stack.append('(')
            backtrack(openCount + 1, closeCount)
            stack.pop()

        if closeCount < openCount:
            stack.append(')')
            backtrack(openCount, closeCount + 1)
            stack.pop()

    backtrack(0, 0)
    return res


print(generateParenthesis(1))
print(generateParenthesis(3))
