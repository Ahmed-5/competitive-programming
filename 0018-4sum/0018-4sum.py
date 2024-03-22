class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        sums = set()
        
        for a in range(n-3):
            for b in range(a+1, n-2):
                t = nums[a]+nums[b]
                
                d = n-1
                c = b+1
                while d>c:
                    s = t+nums[c]+nums[d]
                    if s == target:
                        sums.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1 
                    elif s < target:
                        c += 1
                    else:
                        d -= 1
                        
                        
        return list(sums)