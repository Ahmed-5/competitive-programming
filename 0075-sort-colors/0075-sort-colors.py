class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zs = 0
        os = 0
        ts = 0
        i = 0
        
        while zs+os+ts < len(nums):
            v = nums[i]
            if v == 0:
                if os>0:
                    nums[zs], nums[i] = nums[i], nums[zs]
                if ts>0:
                    nums[zs+os], nums[i] = nums[i], nums[zs+os]
                    
                zs += 1
                
            elif v == 1:
                if ts>0:
                    nums[zs+os], nums[i] = nums[i], nums[zs+os]
                os += 1
                
            elif v == 2:
                ts += 1
                
            i += 1
                