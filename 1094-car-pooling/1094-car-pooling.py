from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = defaultdict(int)
        
        for t in trips:
            n, s, e = t
            d[s] += n
            d[e] -= n
            
        arr = sorted([[i, d[i]] for i in d])
        arr = [i[1] for i in arr]
        
        s = 0
        for i in arr:
            s += i
            if s>capacity:
                return False
            
        return True
            