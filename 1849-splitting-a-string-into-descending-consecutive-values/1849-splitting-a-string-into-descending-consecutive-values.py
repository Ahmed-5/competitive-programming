class Solution:
    def splitString(self, s: str) -> bool:
        arr = []
        solved = [False]
        
        def split(start):
            for i in range(start+1, len(s)+1):
                d = int(s[start:i])
                
                if len(arr)>0 and  arr[-1]<=d:
                    return
                
                elif len(arr)>0 and  arr[-1]-d !=1:
                    continue
                
                arr.append(d)
                if len(arr)>1 and i==len(s):
                    print("Solved", arr)
                    solved[0] = True
                    return 
                split(i)
                if solved[0]:
                    return
                arr.pop()
                
        split(0)
        
        print(arr)
        
        return solved[0]