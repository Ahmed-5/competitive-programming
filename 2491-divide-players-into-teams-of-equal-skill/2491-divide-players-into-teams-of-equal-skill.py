class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        n2 = int(n//2)
        t = []
        total = skill[0] + skill[-1]
        ch = 0
        
        for i in range(n2):
            s = skill[i] + skill[-1-i]
            if total != s:
                return -1
            ch += skill[i] * skill[-1-i]    
            
        return ch