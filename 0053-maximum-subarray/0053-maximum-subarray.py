class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        s = nums[0]
        
        if s<0:
            s = 0
        
        n = len(nums)
        for i in range(1,n):
            s += nums[i]
            if s>max_sum:
                max_sum = s
            if s<0:
                s = 0
        
        return max_sum