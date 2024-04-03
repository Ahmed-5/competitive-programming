class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ts = 0
        fs = 0
        start = 0
        n = len(answerKey)
        streak = 0
        
        for e in range(n):
            c = answerKey[e]
            if c == 'T':
                ts += 1
            else:
                fs += 1
                
            while start<=e and min(ts, fs)>k:
                c = answerKey[start]
                if c == 'T':
                    ts -= 1
                else:
                    fs -= 1
                start += 1
                
            streak = max(streak, ts+fs)
            
        return streak
        