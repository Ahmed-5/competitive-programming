class Solution:
    def removeStars(self, s: str) -> str:
        l = []
        for i in s:
            if i == "*" and len(l)>0:
                l.pop()
            else:
                l.append(i)
        
        return ''.join(l)