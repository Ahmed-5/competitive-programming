class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        
        inds = []
        for ind, i in enumerate(nums):
            if i>target:
                break
            if i == target:
                inds.append(ind)
                
                
        return inds
        