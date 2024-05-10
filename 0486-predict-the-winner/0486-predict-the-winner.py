class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        arr = [[0 for i in nums] for i in nums]
        n = len(nums)
        
        for i in range(n):
            arr[i][i] = nums[i]
            
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                d1 = nums[i] - arr[i+1][j]
                d2 = nums[j] - arr[i][j-1]
                arr[i][j] = max(d1, d2)
        
        # for l in arr:
        #     print(l)
        
        return arr[0][n-1]>=0