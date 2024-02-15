class UndergroundSystem:

    def __init__(self):
        self.checkins = dict()
        self.journeys = dict()
        self.times = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        j = f"{self.checkins[id][0]}-{stationName}"
        tt = t - self.checkins[id][1]
        if j in self.journeys:
            self.journeys[j] += tt
            self.times[j] += 1
        else:
            self.journeys[j] = tt
            self.times[j] = 1
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        j = f"{startStation}-{endStation}"
        t = self.journeys[j]
        ts = self.times[j]
        avg = t/ts
        
        return avg
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)