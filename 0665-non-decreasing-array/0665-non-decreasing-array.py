class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        decreases = 0
        prev = -1_000_000
        current = nums[0]
        for i in nums[1:]:
            if i<current:
                decreases += 1
                if current!=prev and prev<=i:
                    current = i
                else:
                    prev = current
            else:
                prev = current
                current = i

        return decreases<2
        