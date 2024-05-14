from collections import Counter
from bisect import bisect_left

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.scores = Counter()
        self.time_leader = {}
        lead = -1
        
        for p, t in zip(persons, times):
            self.scores[p] += 1
            if self.scores[p]>=self.scores[lead]:
                lead = p
            self.time_leader[t] = lead
            
        print(self.time_leader)
                

    def q(self, t: int) -> int:
        ind = bisect_left(self.times, t)
        ind = min(ind, len(self.times)-1)
        v = self.times[ind]
        if v>t:
            v = self.times[ind-1]
        return self.time_leader[v]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)