class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        start = 0
        end = 0
        length = 0
        n = len(s)
        
        while start<n:
            while end<n:
                c = s[end]
                if c not in d:
                    d[c] = 1
                else:
                    d[c] += 1
                end += 1
                if d[c] > 1:
                    d[c] -= 1
                    end -= 1
                    break
                
            diff = end-start
            length = max(length, diff)
            cc = s[start]
            d[cc] -= 1
            start += 1
            
        return length