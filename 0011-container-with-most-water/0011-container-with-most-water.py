class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        
        start = 0
        end = n-1
        
        h = min(height[start], height[end])
        max_water = h*(end-start)
        
        while start<end:
            h = min(height[start], height[end])
            water = h*(end-start)
            
            if water > max_water:
                max_water = water
                
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
                
        return max_water