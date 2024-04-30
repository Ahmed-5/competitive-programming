class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        m = n
        while m%4==0:
            m = int(m//4)
            
        if m==1:
            return True
        return False