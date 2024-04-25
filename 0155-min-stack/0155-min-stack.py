class MinStack:

    def __init__(self):
        self.stack = []
        self.l = []
        

    def push(self, val: int) -> None:
        if len(self.stack)==0 or val <= self.stack[-1]:
            self.stack.append(val)
        self.l.append(val)
        

    def pop(self) -> None:
        if len(self.l)>0:
            val = self.l.pop()
            if val == self.stack[-1]:
                self.stack.pop()
        

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()