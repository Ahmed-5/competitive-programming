class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0
        n = len(nums)
        e = n-1
        ind = -1
        
        while s<=e:
            mid = int((s+e)//2)
            v = nums[mid]
            if v == target:
                ind = mid
                break
            elif v > target:
                e = mid-1
                ind = mid
            else:
                ind = mid+1
                s = mid+1
                
        return ind