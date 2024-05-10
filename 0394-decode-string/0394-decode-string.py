class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        ss = ""
        
        for i in s:
            if i in "0123456789":
                num = num*10 + int(i)
                
            elif i == "[":
                stack.append([num, ss])
                ss = ""
                num = 0
                
            elif i == "]":
                num2, prev = stack.pop()
                ss = prev+num2*ss
            
            else:
                ss += i
                
        return ss