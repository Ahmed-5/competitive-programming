class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<4:
            return min(nums)
        
        if nums[-1]>nums[0]:
            return nums[0]
        
        else:
            n = len(nums)
            s = 0
            e = n-1
            while s<e:
                mid = int((s+e)//2)
                if nums[mid-1]<nums[mid] and nums[mid]>nums[0]:
                    s = mid+1
                else:
                    e = mid
                    
            return min(nums[s%n], nums[(s+1)%n])
                