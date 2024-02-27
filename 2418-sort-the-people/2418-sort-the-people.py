class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        l = [[] for i in range(100001)]
        for i in range(n):
            l[heights[i]].append(names[i])
            
        ns = []
        for i in l[::-1]:
            ns.extend(i)
                    
        return ns
                    
        