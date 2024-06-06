class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)<2:
            return ""
        
        chars = set(s)
        
        for ind, c in enumerate(s):
            if c.swapcase() not in chars:
                sl = self.longestNiceSubstring(s[:ind])
                sr = self.longestNiceSubstring(s[ind+1:])
                if len(sl)>=len(sr):
                    return sl
                else:
                    return sr
                
        return s