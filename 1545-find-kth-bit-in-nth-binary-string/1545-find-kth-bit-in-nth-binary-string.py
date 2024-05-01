class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        d = {"0":"1", "1":"0"}
        
        s = "0"
        
        for i in range(1,n):
            inv = "".join([d[i] for i in s])
            inv = inv[::-1]
            s = f"{s}1{inv}"
            # print(i+1, s)
        
        return s[k-1]