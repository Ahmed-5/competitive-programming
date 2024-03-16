class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        n2 = int(n//2)
        pal_a = True
        across_a = True
        continued_a = False
        pal_b = True
        across_b = True
        continued_b = False
        
        for i in range(n2):
            if across_a:
                if a[i] != b[n-1-i]:
                    across_a = False
                    
            if not across_a:
                if a[i] != a[n-i-1]:
                    pal_a = False
                    
            if across_b:
                if b[i] != a[n-1-i]:
                    across_b = False
                    
            if not across_b:
                if b[i] != b[n-i-1]:
                    pal_b = False
                    
        if pal_a or pal_b:
            return True
        
        pal_a = True
        across_a = True
        continued_a = False
        pal_b = True
        across_b = True
        continued_b = False
        
        for i in range(n2):
            if across_a:
                if a[i] != b[n-1-i]:
                    across_a = False
                    
            if not across_a:
                if not(b[i] == b[n-i-1]):
                    pal_a = False
                    
            if across_b:
                if b[i] != a[n-1-i]:
                    across_b = False
                    
            if not across_b:
                if not(a[i] == a[n-i-1]):
                    pal_b = False
                    
        return pal_a or pal_b