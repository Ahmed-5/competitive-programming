class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        level = 0
        score = 0
        for ind, i in enumerate(s):
            if i == "(":
                level += 1
            else:
                level -= 1
                if s[ind-1] == "(":
                    score += 2**level
                
        return score