from random import choice

class RandomizedSet:

    def __init__(self):
        self.d = dict()
        self.l = []
        

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        ind = self.d[val]
        del self.d[val]
        new_val = self.l.pop()
        if new_val != val:
            self.l[ind] = new_val
            self.d[new_val] = ind
        return True
        

    def getRandom(self) -> int:
        return choice(self.l)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()