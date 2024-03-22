class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sp = "".join(sorted(p))
        lp = len(p)
        ls = len(s)
        n = ls-lp+1
        inds = []
        
        for i in range(n):
            ss = s[i:i+lp]
            sss = "".join(sorted(ss))
            if sss == sp:
                inds.append(i)
        
        return inds