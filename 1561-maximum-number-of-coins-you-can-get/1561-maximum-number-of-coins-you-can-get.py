class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n3 = len(piles)
        n = int(n3/3)
        s = 0
        
        piles.sort()
        piles = piles[::-1]
        
        for i in range(n):
            s += piles[2*i+1]
            
        return s
        