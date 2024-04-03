from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt = defaultdict(int)
        ds = defaultdict(int)
        sett = set(t)
        sets = set()
        n = len(s)
        
        for i in t:
            dt[i]+=1
            
        ss = f"{s}-"
        start = 0
        for e in range(n):
            c = s[e]
            ds[c] += 1
            sets.add(c)
            if sets>=sett:
                while start<=e and sets>=sett:
                    l1 = e-start+1
                    l2 = len(ss)
                    if l1<l2:
                        b = False
                        for letter in dt:
                            if dt[letter]>ds[letter]:
                                b = True
                                break
                        if b:
                            break
                        ss = s[start:e+1]
                    c = s[start]
                    ds[c] -= 1
                    if ds[c]==0:
                        del ds[c]
                        sets.discard(c)
                    start += 1
            
        if ss[-1] == "-":
            return ""
        return ss