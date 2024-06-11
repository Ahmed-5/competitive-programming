class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        s0 = set(edges[0])
        s1 = set(edges[1])
        s = list(set.intersection(s0, s1))
        return s[0]