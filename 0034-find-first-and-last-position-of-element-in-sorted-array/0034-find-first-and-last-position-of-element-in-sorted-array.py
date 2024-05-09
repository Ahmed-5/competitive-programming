class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        s = 0
        e = n-1
        
        start = n
        end = -1
        
        while s<=e:
            mid = int((s+e)//2)
            v = nums[mid]
            if v <= target:
                print(v)
                if v == target:
                    end = max(mid, end)
                s = mid+1
            else:
                e = mid-1
                
        s = 0
        e = n-1
        
        while s<=e:
            mid = int((s+e)//2)
            v = nums[mid]
            if v < target:
                s = mid+1
            else:
                if v == target:
                    end = max(mid, end)
                    start = min(mid, start)
                e = mid-1
                
        if start == n:
            start = -1
            
        return [start, end]