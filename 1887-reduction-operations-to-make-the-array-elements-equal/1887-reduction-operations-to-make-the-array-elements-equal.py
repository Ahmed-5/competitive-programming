class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        inds = {}
        
        ns = sorted(list(set(nums)))
        
        if len(ns) == 1:
            return 0
        
        for ind, i in enumerate(nums):
            if i not in inds:
                inds[i] = 1
            else:
                inds[i] += 1
            
        s = 0
        for ind, i in enumerate(ns):
            s += ind*inds[i]
            
        return s
        