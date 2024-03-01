class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zs = [0 for i in nums]
        os = [0 for i in nums]
        
        cz = 0
        co = 0
        
        n = len(nums)
        
        for i in range(n):
            if nums[i] == 0:
                cz += 1
            elif nums[i] == 1:
                co += 1
                
            zs[i] = cz
            os[i] = co
                
        max_score = co
        inds = [0]
        
        for i in range(n):
            score = zs[i] + os[-1] - os[i]
            if score > max_score:
                inds = [i+1]
                max_score = score
            elif score == max_score:
                inds.append(i+1)
                
        return inds