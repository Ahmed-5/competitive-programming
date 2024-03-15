class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ind_a = 0
        ind_b = 0
        n1 = len(firstList)
        n2 = len(secondList)
        inter = []
        
        while ind_a<n1 and ind_b<n2:
            x1, x2 = firstList[ind_a]
            y1, y2 = secondList[ind_b]
            
            if x1<=y1<=x2 or y1<=x1<=y2:
                m1 = max(y1, x1)
                m2 = min(y2, x2)
                
                inter.append([m1, m2])
                
            if y2>x2:
                ind_a += 1
            else:
                ind_b += 1
                
        return inter