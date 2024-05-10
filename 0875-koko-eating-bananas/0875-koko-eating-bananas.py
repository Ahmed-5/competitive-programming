from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        e = 0
        
        for i in piles:
            e = max(e, i)
            
        while s<e:
            mid = (s+e)//2
            hs = 0
            for i in piles:
                hs += ceil(i/mid)
                
            # print(mid, hs, s, e)
                
            if hs <= h:
                e = mid
            else:
                s = mid+1
                
        return s
            