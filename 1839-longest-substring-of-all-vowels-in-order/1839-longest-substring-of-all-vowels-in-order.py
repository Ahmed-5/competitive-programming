class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        max_len = 0
        l = 0
        current = -1
        vowels = {'a':0, 'e':1, "i":2, 'o':3, "u":4}
        
        for i in word:
            v = vowels[i]
            if v==current or v==1+current:
                current = v
                l += 1
            else:
                if v==0:
                    l=1
                    current = 0
                else:
                    l=0
                    current=-1
            
            if current == 4:
                max_len = max(l, max_len)
            
        return max_len