class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefix = [0]
        ps = 0
        suffix = [0]
        ss = 0
        
        for i in range(k):
            ps += cardPoints[i]
            prefix.append(ps)
            ss += cardPoints[-i-1]
            suffix.append(ss)
        
        m = 0
        for i in range(k+1):
            # print(prefix[i], suffix[-i-1])
            s = prefix[i]+suffix[-i-1]
            m = max(m, s)
            
        return m
        