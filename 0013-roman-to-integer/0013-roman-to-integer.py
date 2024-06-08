class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,}
        
        s = s[::-1]
        num = 0
        
        prev = 0
        for i in s:
            v = d[i]
            if v < prev:
                num -= v
            else:
                num += v
                prev = v
            
        return num
        