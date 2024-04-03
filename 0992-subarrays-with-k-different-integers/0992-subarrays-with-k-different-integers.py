from collections import defaultdict

class Solution:
    def countAtMost(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        n = len(nums)
        start = 0
        ks = 0
        
        for e in range(n):
            c = nums[e]
            d[c] += 1
            
            while start<=e and len(d)>k:
                c = nums[start]
                d[c] -= 1
                if d[c] == 0:
                    del d[c]
                    
                start += 1
                    
            ks += e-start+1
            
        return ks
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ks = self.countAtMost(nums, k)
        k1s = self.countAtMost(nums, k-1)
            
        return ks-k1s