class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.end = -1
        self.start = 0
        self.l = [None for i in range(k)]
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        ind = (self.start-1)%self.k
        self.l[ind] = value
        self.start -= 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        ind = (self.end+1)%self.k
        self.l[ind] = value
        self.end += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        ind = (self.start)%self.k
        self.l[ind] = None
        self.start += 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        ind = (self.end)%self.k
        self.l[ind] = None
        self.end -= 1
        return True
        

    def getFront(self) -> int:
        ind = (self.start)%self.k
        if self.l[ind] is not None:
            return self.l[ind]
        return -1
        

    def getRear(self) -> int:
        ind = (self.end)%self.k
        if self.l[ind] is not None:
            return self.l[ind]
        return -1
        

    def isEmpty(self) -> bool:
        return self.end<self.start
        

    def isFull(self) -> bool:
        return self.end-self.start==self.k-1
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()