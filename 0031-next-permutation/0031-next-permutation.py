class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2
        while i>=0 and nums[i] >= nums[i+1]:
            i-=1
            
        if i<0:
            nums.reverse()
            return
            
        j=n-1
        while j>=i and nums[j]<=nums[i]:
            j-=1
            
        nums[i], nums[j] = nums[j], nums[i]
        s = i+1
        e = int((s+n+1)//2)
        
        for i in range(s, e):
            ind = n-1-(i-s)
            nums[i], nums[ind] = nums[ind], nums[i]