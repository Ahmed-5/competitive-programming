class Solution:
    def isValid(self, s: str) -> bool:
        d = {"{":"}", "(":")", "[":"]"}
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif len(stack)>0:
                l = stack.pop()
                if i != d[l]:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        return False
        