class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)-k+1
        max_s = sum(nums[:k])
        s = sum(nums[:k])
        
        for i in range(1,n):
            s -= nums[i-1]
            s += nums[i+k-1]
            max_s = max(max_s, s)
            
        return round(max_s/k, 5)
        