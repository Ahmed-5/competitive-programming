class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s1 = 0
        s2 = sum(nums[1:])
        ind = 0
        n = len(nums)
        
        for i in range(n):
            if s1 == s2:
                return ind
            
            s1 += nums[ind]
            ind += 1
            if ind<n:
                s2 -= nums[ind]
            
        return -1