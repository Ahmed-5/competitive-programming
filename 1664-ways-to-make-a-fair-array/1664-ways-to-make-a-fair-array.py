class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        prefix = [[0, 0]]
        n = len(nums)
        
        for i in range(n):
            mod = i%2
            l = [i for i in prefix[-1]]
            l[mod] += nums[i]
            
            prefix.append(l)
            
        # print(prefix)
        
        suffix = [[0,0]]
        
        for i in range(n-1,-1,-1):
            mod = 1 - (i%2)
            l = [i for i in suffix[-1]]
            l[mod] += nums[i]
            
            suffix.append(l)
            
        suffix.reverse()
        # print(suffix)
        
        count = 0
        
        for i in range(n):
            odds = prefix[i][1] + suffix[i+1][1]            
            evens = prefix[i][0] + suffix[i+1][0]
            if odds == evens:
                count += 1
        
        return count