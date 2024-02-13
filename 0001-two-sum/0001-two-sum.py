class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = [(n, i) for i,n in enumerate(nums)]
        
        l.sort()
        
        s = 0
        e = len(l) - 1
        
        while s<e:
            summ = l[s][0] + l[e][0]
            if summ == target:
                return l[s][1], l[e][1]
            elif summ < target:
                s += 1
            elif summ > target:
                e -= 1
            
        