class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.list = [None for _ in range(n)]
        self.current_index = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list[idKey-1] = value
        l = []
        while(self.current_index<self.n and self.list[self.current_index]):
            l.append( self.list[self.current_index])
            self.current_index += 1
        return l
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)