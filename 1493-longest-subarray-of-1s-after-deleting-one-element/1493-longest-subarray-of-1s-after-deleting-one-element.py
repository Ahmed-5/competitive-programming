class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        not_ones = 0
        n = len(nums)
        start = 0
        l = 0
        max_l = -1
        
        for end in range(n):
            l += 1
            if nums[end] != 1:
                not_ones += 1
                
            while start<=end and not_ones>1:
                if nums[start] != 1:
                    not_ones -= 1
                start += 1
                l -= 1
                
            max_l = max(l-1, max_l)
            
        return max_l
            