from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        s = 0
        d = defaultdict(int)
        d[0] += 1
        
        for i in nums:
            s += i
            diff = s-k
            if diff in d:
                count += d[diff]
            d[s] += 1
            
        return count