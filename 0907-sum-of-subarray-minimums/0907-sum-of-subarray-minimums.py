class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        s = 0
        n = len(arr)
        
        for ind, i in enumerate(arr):
            while len(stack)>0 and stack[-1][0]>=i:
                i2, ind2 = stack.pop()
                if len(stack)>0:
                    l1 = ind2 - stack[-1][1]
                else:
                    l1 = ind2+1
                l2 = ind-ind2
                inc = l2*l1*i2
                # print(i2, ind2, l1, l2, inc)
                s += inc
                s = s%1_000_000_007
                # print(s)
                
            stack.append([i, ind])
            
        while len(stack)>0:
            i, ind = stack.pop()
            if len(stack)>0:
                l1 = ind - stack[-1][1]
            else:
                l1 = ind+1
            l2 = n-ind
            inc = l2*l1*i
            # print(i, ind, l1, l2, inc)
            s += inc
            s = s%1_000_000_007
            # print(s)
            
        return s