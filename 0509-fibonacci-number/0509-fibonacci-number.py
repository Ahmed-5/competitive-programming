class Solution:
    def fib(self, n: int) -> int:
        n0 = 0
        n1 = 1
        
        for i in range(n):
            n0, n1 = n1, n0+n1
            
        return n0
        