class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        n = len(nums)
        half = int(n//2)
        m = nums[0] + nums[-1]
        for i in range(half):
            current = nums[i] + nums[-i-1]
            if current>m:
                m = current
                
        return m
            
        