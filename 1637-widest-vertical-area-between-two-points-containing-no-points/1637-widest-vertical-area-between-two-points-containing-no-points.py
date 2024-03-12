class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = [i[0] for i in points]
        xs.sort()
        n = len(xs)
        
        max_diff = 0
        
        for i in range(n-1):
            max_diff = max(max_diff, xs[i+1]-xs[i])
            
        return max_diff