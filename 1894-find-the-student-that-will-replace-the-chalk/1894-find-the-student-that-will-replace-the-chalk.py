class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = 0
        n = len(chalk)
        prefix = []
        for i in chalk:
            s += i
            prefix.append(s)
            
        d = k%s
        for i in range(n):
            if d<prefix[i]:
                return i