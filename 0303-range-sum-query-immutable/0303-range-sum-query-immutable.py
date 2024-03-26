class NumArray:

    def __init__(self, nums: List[int]):
        self.ranges = [0]
        s = 0
        n = len(nums)
        
        for i in range(n):
            s += nums[i]
            self.ranges.append(s)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.ranges[right+1]-self.ranges[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)