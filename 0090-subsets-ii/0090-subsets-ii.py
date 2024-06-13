from collections import defaultdict

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
            
        keys = list(d.keys())
            
        s = []
        
        def subsets(ind=0, current=[]):
            if ind==len(keys):
                s.append(current)
                return
                
            i = keys[ind]
            n = d[i]
            for count in range(n+1):
                subsets(ind+1, current+[i for _ in range(count)])
                
        subsets()
        
        return s
            