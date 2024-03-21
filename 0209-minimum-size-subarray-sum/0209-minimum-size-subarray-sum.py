class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        s = nums[0]
        n = len(nums)
        l = 1_000_000
        
        while right<n:
            if s<target:
                right += 1
                if right<n:
                    s += nums[right]
            else:
                l = min(l, right-left+1)
                s -= nums[left]
                left += 1
                
        if l == 1_000_000:
            return 0
        else:
            return l
        