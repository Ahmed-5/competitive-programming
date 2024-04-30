class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        m = n
        while m%3==0:
            m = int(m//3)
            
        if m==1:
            return True
        return False