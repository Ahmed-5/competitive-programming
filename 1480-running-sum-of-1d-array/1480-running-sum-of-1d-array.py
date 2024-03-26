class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = 0
        
        for i in range(n):
            s += nums[i]
            nums[i] = s
            
        return nums
        