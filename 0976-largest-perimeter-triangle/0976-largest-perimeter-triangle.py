class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        for i in range(len(nums)-2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            
            if (b+c>a>b-c):
                return a+b+c
            
        return 0
        