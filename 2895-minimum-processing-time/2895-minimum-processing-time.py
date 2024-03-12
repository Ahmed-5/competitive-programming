class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        tasks.reverse()
        
        
        max_time = 0
        n = len(processorTime)
        for i in range(n):
            p = processorTime[i]
            t = tasks[4*i]
            max_time = max(max_time, p+t)
            
        return max_time