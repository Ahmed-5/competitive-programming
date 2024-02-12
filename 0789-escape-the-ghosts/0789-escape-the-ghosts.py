class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist = abs(target[0]) + abs(target[1])
        
        for i in ghosts:
            dist_ghost = abs(i[0]-target[0]) + abs(i[1]-target[1])
            if dist_ghost<=dist:
                return False
        
        return True