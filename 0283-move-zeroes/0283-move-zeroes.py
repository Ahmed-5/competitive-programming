class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        first_zero = 0
        
        for i in range(n):
            while first_zero < n:
                if nums[first_zero] == 0:
                    break
                first_zero += 1
                
            if first_zero >= n:
                break
            
            if i > first_zero and nums[i] != 0:
                nums[i], nums[first_zero] = nums[first_zero], nums[i]        