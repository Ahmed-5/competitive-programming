class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hare = nums[nums[0]]
        turtle = nums[0]
        
        while hare != turtle:
            hare = nums[nums[hare]]
            turtle = nums[turtle]
            
        ind = 0
        while ind != turtle:
            turtle = nums[turtle]
            ind = nums[ind]
            
        return ind