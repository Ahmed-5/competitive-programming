class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val = None
        stack = []
        
        for t in tokens:
            if t in "+-/*":
                n2 = stack.pop()
                n1 = stack.pop()
                op = f"{n1}{t}{n2}"
                val = int(eval(op))
                stack.append(val)
                # print(op)
                # print(stack)
            else:
                val = int(t)
                stack.append(t)
                
        return val
        