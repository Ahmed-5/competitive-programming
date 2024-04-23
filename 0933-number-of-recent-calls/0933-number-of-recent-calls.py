from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque([])
        self.len = 0
        

    def ping(self, t: int) -> int:
        l = t-3000
        while self.len>0 and self.q[-1]<l:
            self.q.pop()
            self.len -= 1
            
        self.q.appendleft(t)
        self.len += 1
        return self.len
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)