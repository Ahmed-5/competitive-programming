class Solution(object):
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        dels = 0
        
        for j in range(m):
            current = 0
            for i in range(n):
                if ord(strs[i][j]) < current:
                    dels+=1
                    break
                current = ord(strs[i][j])
                    
        return dels