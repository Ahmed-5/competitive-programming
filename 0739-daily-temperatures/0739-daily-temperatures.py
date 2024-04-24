class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = []
        inds = [0 for i in temperatures]
        
        for ind, i in enumerate(temperatures):
            while len(l)>0 and i>l[-1][0]:
                i2, ind2 = l.pop()
                inds[ind2] = ind - ind2
                
            l.append([i, ind])
            
        return inds
            
        