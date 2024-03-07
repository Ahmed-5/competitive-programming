import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(math.floor(math.sqrt(c)))
        l = [i**2 for i in range(n+1)]
        
        for i in range(n+1):
            sq = i**2
            rem = c-sq
            sq_rem = int(math.floor(math.sqrt(rem)))
            if sq_rem < i:
                return False
            if sq_rem**2 == rem:
                return True
            
        
        