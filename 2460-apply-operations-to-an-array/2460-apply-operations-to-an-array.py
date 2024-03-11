class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        zeros = 0
        c = False
        if nums[0] == 0:
            zeros += 1
        for i in range(n-1):
            if nums[i+1] == 0:
                zeros += 1
            elif nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                zeros += 1
                c = True
                
        a = []
        for i in nums:
            if i != 0:
                a.append(i)
                
        for i in range(zeros):
            a.append(0)
            
        return a
                