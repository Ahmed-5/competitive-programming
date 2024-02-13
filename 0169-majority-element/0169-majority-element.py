class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        c = Counter(nums)

        res = []

        for i in c:
            if c[i]>n:
                res.append(i)

        res.sort()
        return res[0]
        