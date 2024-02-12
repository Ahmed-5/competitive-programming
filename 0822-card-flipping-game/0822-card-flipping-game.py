from collections import Counter

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        a = set([*fronts, *backs])
            
        doubles = set()
        for i,j in zip(fronts, backs):
            if i==j:
                doubles.add(i)
                
        diff = a - doubles
        if len(diff) > 0:
            return min(diff)
        return 0