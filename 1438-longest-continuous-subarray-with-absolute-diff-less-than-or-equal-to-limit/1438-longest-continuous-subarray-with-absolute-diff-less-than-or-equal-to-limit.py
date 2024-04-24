from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq = deque([])
        maxq = deque([])
        
        n = len(nums)
        start = 0
        max_len = 0
        for e in range(n):
            el = nums[e]
            while minq and nums[minq[0]]>el:
                minq.popleft()
            minq.appendleft(e)
            
            while maxq and nums[maxq[0]]<el:
                maxq.popleft()
            maxq.appendleft(e)
            
            while nums[maxq[-1]]-nums[minq[-1]]>limit:
                if start==maxq[-1]:
                    maxq.pop()
                    
                if start==minq[-1]:
                    minq.pop()
                    
                start += 1
                
            diff = e-start+1
            max_len = max(max_len, diff)
            
        return max_len
            