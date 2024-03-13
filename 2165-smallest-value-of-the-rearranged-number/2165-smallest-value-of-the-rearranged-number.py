class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = [i for i in str(num)]
        s = ""
        if nums[0] == "-":
            s += "-"
            nums = nums[1:]
            nums.sort(reverse=True)
            for i in nums:
                s += i
        else:
            nums.sort()
            zs = 0
            for i in nums:
                if i == "0":
                    zs += 1
                else:
                    break

            for i in nums[zs:]:
                s += i
                if len(s) == 1:
                    for _ in range(zs):
                        s += "0"
                    
        return int(s) if s else 0