class Solution:
    def countGoodNumbers(self, n: int) -> int:
        no = int(n//2)
        ne = n-no
        
        s = pow(5, ne, 1_000_000_007)
        s *= pow(4, no, 1_000_000_007)
        
        s = s%1_000_000_007
        
        return s