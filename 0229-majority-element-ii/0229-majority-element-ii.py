from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        c = Counter(nums)

        res = []

        for i in c:
            if c[i]>n:
                res.append(i)

        res.sort()
        return res
        