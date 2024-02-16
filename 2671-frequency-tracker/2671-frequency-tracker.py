from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.nums = defaultdict(int)
        self.freqs = [0]

    def add(self, number: int) -> None:
        self.nums[number] += 1
        freq = self.nums[number]
        if len(self.freqs)<=freq:
            self.freqs.append(1)
        else:
            self.freqs[freq] += 1
        self.freqs[freq-1] -= 1
        

    def deleteOne(self, number: int) -> None:
        if self.nums[number] > 0:
            freq = self.nums[number]
            self.nums[number] -= 1
            self.freqs[freq] -= 1
            self.freqs[freq-1] += 1
        

    def hasFrequency(self, frequency: int) -> bool:            
        return len(self.freqs)>frequency and self.freqs[frequency]>0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)