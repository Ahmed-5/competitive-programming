from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        d = defaultdict(int)
        start = 0
        m = 0
        
        for e in range(n):
            f = fruits[e]
            d[f] += 1
            
            while start<=e and len(d)>2:
                fs = fruits[start]
                d[fs] -= 1
                if d[fs] == 0:
                    del d[fs]
                start += 1
                
            s = 0
            for i in d:
                s += d[i]
            m = max(m, s)
                
        return m