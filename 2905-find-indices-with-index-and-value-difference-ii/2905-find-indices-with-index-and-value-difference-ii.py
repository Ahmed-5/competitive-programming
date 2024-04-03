class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        d = indexDifference
        vd = valueDifference
        n = len(nums)
        prefix = [[nums[0], 0]]
        suffix = [[nums[-1], n-1]]
        for i in range(1, n-d):
            m = prefix[-1]
            if nums[i]>m[0]:
                m = [nums[i], i]
            prefix.append(m)
            
            m = suffix[-1]
            if nums[n-i-1]>m[0]:
                m = [nums[n-i-1], n-i-1]
            suffix.append(m)
            
        suffix.reverse()
        
        for i in range(n):
            v = nums[i]
                
            if d-1<i:
                v2, i2 = prefix[i-d]
                if abs(i2-i)>=d and abs(v-v2)>=vd:
                    return [i, i2]
                
            if i<n-d:
                v2, i2 = suffix[i]
                if abs(i2-i)>=d and abs(v-v2)>=vd:
                    return [i, i2]
                
        return [-1, -1]
                