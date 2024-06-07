from collections import defaultdict

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        d = defaultdict(int)
        
        for c in candidates:
            d[c] += 1
            
        ks = list(d.keys())
        visited = [False for i in ks]
        
        def combinations(target, l=[], start=0):
            if target<0 or start>=len(ks):
                return
            elif target==0:
                ans.append(l)
                return
            
            for ind, i in enumerate(ks[start:]):
                if visited[start+ind]:
                    continue
                    
                visited[start+ind]=True
                for j in range(1, d[i]+1):
                    combinations(target-i*j, l+[i for _ in range(j)], start+ind)
                visited[start+ind]=False
                
        combinations(target)
        
        return ans