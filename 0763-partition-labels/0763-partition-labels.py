class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        inds = {c:i for i, c in enumerate(s)}
        res = []
        
        start = 0
        end = 0
        n = len(s)
        
        for i in range(n):
            c = s[i]
            end = max(end, inds[c])
            
            if i==end:
                res.append(end-start+1)
                start = i+1
                
                
        return res
        