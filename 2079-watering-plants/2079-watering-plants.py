class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        stops = []
        n = len(plants)
        
        current_capacity = capacity
        for i,e in enumerate(plants):
            if current_capacity >= e:
                current_capacity -= e
            else:
                current_capacity = capacity - e
                stops.append(i)
                
        s = 2*sum(stops) + n
        
        return s
        