class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        matches = 0
        players.sort(reverse=True) 
        ps = len(players)
        trainers.sort(reverse=True)
        ts = len(trainers)
        
        p = 0
        t = 0
        
        while p < ps and t < ts:
            if players[p] <= trainers[t]:
                matches += 1
                t += 1
            p += 1
            
        return matches