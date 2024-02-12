class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = [i for i,e in enumerate(boxes) if e=='1']
        n = len(ones)
        s = sum(ones)
        
        ans = []
        for i in range(len(boxes)):
            ds = 0
            for j in ones:
                ds += abs(i-j)
            ans.append(ds)
        return ans
        