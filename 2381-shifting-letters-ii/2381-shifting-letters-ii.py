class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        l = [0 for _ in range(n)]
        
        for shift in shifts:
            ss, e, sh = shift
            if sh == 0:
                sh = -1
                
            l[ss] += sh
            if e+1<n:
                l[e+1] -= sh
                
        ss = 0
        for i in range(n):
            ss += l[i]
            l[i] = ss
            
        sl = [ord(i)-ord('a') for i in s]
        for i in range(n):
            j = (sl[i]+l[i])%26
            j = chr(j+ord('a'))
            sl[i] = j
            
            
        return "".join(sl)