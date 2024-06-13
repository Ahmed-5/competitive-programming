class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustee = [0 for i in range(n)]
        trusted = [0 for i in range(n)]
        
        for te, td in trust:
            trustee[te-1] += 1
            trusted[td-1] += 1
            
        sol = []
        for ind in range(n):
            i = trustee[ind]
            j = trusted[ind]
            if j==n-1 and i==0:
                sol.append(ind)
                
        if len(sol)!=1:
            return -1
        else:
            return sol[0]+1
        