class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        n = len(nums)
        subs = 0
        prod = 1
        
        for i, end in enumerate(nums):
            prod *= end
            
            while start <= i and prod>=k:
                prod = int(prod/nums[start])
                start += 1
                
            subs += i - start + 1
                    
        return subs