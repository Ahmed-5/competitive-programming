from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = [[0 for i in range(n)] for j in range(n)]
        r = defaultdict(int)
        
        for i,j in roads:
            g[i][j] = 1
            g[j][i] = 1
            r[i] += 1
            r[j] += 1
            
        m = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                m = max(r[i]+r[j]-g[i][j], m)
                
        return m