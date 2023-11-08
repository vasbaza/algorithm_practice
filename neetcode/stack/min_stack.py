class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minVals:
            self.minVals = [val]
        else:
            if val < self.minVals[-1]:
                self.minVals.append(val)
            else:
                self.minVals.append(self.minVals[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minVals.pop()

    def top(self) -> int:
        print(self.stack[-1])
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.minVals[-1])
        return self.minVals[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.push(-4)
minStack.push(-7)
minStack.push(10)
minStack.pop()
minStack.pop()
minStack.getMin()