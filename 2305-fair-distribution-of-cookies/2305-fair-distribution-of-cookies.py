class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        sol = [None]
        ks = [0 for i in range(k)]
        
        def recurse(start):
            if start == len(cookies):
                m1 = max(ks)
                if sol[0]:
                    sol[0] = min(sol[0], m1)
                else:
                    sol[0] = m1
                return
            
            for i in range(k):
                ks[i] += cookies[start]
                recurse(start+1)
                ks[i] -= cookies[start]
                
                if ks[i] == 0:
                    return
                
        recurse(0)
        
        return sol[0]