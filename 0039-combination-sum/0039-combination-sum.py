class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def combinations(target, l=[], start=0):
            if target<0 or start>=len(candidates):
                return
            elif target==0:
                ans.append(l)
                return
            
            for ind, i in enumerate(candidates[start:]):
                combinations(target-i, l+[i], ind+start)
                
        combinations(target)
        
        return ans