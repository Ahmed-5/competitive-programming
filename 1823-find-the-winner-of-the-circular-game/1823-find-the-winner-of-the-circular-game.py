class Solution:    
    def findTheWinner(self, n: int, k: int) -> int:
        l = [i+1 for i in range(n)]
        start = 0
        while (len(l)>1):
            loser = (start+k-1)%len(l)
            l.pop(loser)
            start = loser%len(l)
            
        return l[0]