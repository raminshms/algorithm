def evalRPN(tokens):
    stack = []
    for t in tokens:
        if t == '+':
            stack.append(stack.pop() + stack.pop())
        elif t == '*':
            stack.append(stack.pop() * stack.pop())
        elif t == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif t == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(t))

    return stack[-1]


print(evalRPN(["1", "2", "+", "3", "*", "4", "-"]))
print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["4", "13", "5", "/", "+"]))
print(evalRPN(["10", "6", "9", "3", "+", "-11",
      "*", "/", "*", "17", "+", "5", "+"]))
