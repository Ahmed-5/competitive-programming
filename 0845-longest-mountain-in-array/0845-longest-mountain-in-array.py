class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        streak = 0
        inc = 0
        dec = 0
        climb = 0
        n = len(arr)
        
        for i in range(n-1):
            if arr[i]<arr[i+1]:
                if climb != 1:
                    if climb == -1 and dec>0 and inc>0:
                        s = inc + dec
                        streak = max(streak, s)
                    climb = 1
                    inc = 2
                    dec = 0
                else:
                    inc += 1
            elif arr[i]>arr[i+1]:
                if climb != -1:
                    dec = 1
                    climb = -1
                else:
                    dec += 1
            else:
                if climb == -1 and dec>0 and inc>0:
                    s = inc + dec
                    streak = max(streak, s)
                inc = 0
                dec = 0
                climb = 0
                ss=0
        
        if dec>0 and inc>0:
            s = inc + dec
            streak = max(streak, s)
        
        return streak