class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        m = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(m)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


def test1():
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(0)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())


def test2():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())


def test3():
    minStack = MinStack()
    minStack.push(2)
    minStack.push(0)
    minStack.push(3)
    minStack.push(0)
    print(minStack.getMin())
    minStack.pop()

    print(minStack.getMin())
    minStack.pop()

    print(minStack.getMin())
    minStack.pop()

    print(minStack.getMin())


test1()
test2()
test3()
