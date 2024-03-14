class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        s = 0
        e = len(people)-1
        
        boats = 0
        
        while s <= e:
            w = people[s] + people[e]
            boats += 1
            e -= 1
            if w <= limit:
                s += 1
                
        return boats