class Solution:
    def minOperations(self, logs: List[str]) -> int:
        levels = 0
        for i in logs:
            if i == "../":
                levels = max(0, levels-1)
            elif i == "./":
                levels += 0
            else:
                levels += 1
                
                
        return levels
        