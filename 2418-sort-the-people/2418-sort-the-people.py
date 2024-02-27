class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n-1):
            ind = -1
            maxx = 0
            for j in range(i, n):
                if heights[j]>maxx:
                    ind = j
                    maxx = heights[j]
            if ind != -1:
                heights[i], heights[ind] = heights[ind], heights[i]
                names[i], names[ind] = names[ind], names[i]
                    
        return names
                    
        