class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = 0
        e = n-1
        
        while s<=e:
            mid = int((s+e)//2)
            v = nums[mid]
            if v > target:
                e = mid-1
            elif v < target:
                s = mid+1
            else:
                return mid
            
        return -1
        