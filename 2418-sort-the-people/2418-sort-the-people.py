class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(1, n):
            pivot = heights[i]
            for j in range(i-1, -1, -1):
                if heights[j]<pivot:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
                else:
                    break
                    
        return names
                    
        