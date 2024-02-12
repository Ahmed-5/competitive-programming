class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        kid_max = max(candies)
        kids = []
        
        for i in candies:
            kids.append((i+extraCandies)>=kid_max)
            
        return kids
        