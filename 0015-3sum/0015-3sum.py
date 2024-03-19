class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = set()
        n = len(nums)
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[-1]:
                continue
            
            left = i+1
            right = len(nums)-1
            
            while left<right:
                if left == i:
                    left += 1
                    continue
                    
                if right == i:
                    right -= 1
                    continue
                   
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    solutions.add((nums[left], nums[i], nums[right]))
                    right -= 1
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1
                    
        
        return list(solutions)