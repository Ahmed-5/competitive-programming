class Solution:
    def find_row(self, letter: str) -> int:
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        
        if letter in r1:
            return 1
        if letter in r2:
            return 2
        if letter in r3:
            return 3
    
    def findWords(self, words: List[str]) -> List[str]:
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        
        ws = []
        
        for i in words:
            a = i.lower()
            row = self.find_row(a[0])
            same_row = True
            for l in a:
                row_l = self.find_row(l)
                if row_l != row:
                    same_row = False
                    break
                    
            if same_row:
                ws.append(i)
                
        return ws
        