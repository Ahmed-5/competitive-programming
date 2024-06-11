class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        self.solved = False
        def solve(l1, l2):
            n = len(num)
            if self.solved:
                return
            
            if n-l1-l2<max(l1, l2):
                return
            
            s = 0
            e1 = l1
            e2 = l1+l2
            while e2<n:
                i1 = num[s:e1]
                if len(i1)>1 and i1[0]=="0":
                    return
                i1 = int(i1)
                
                i2 = num[e1:e2]
                if len(i2)>1 and i2[0]=="0":
                    return
                i2 = int(i2)
                
                i3 = str(i1+i2)
                print(i1, i2, i3)
                l3 = len(i3)
                e3 = e2+l3
                if e3>n or num[e2:e3]!=i3:
                    return
                s = e1
                e1 = e2
                e2 = e3
                print(i1, i2, i3)
            
            self.solved = True
            
        l = int(len(num)//2)+1
        for i in range(1, l):
            for j in range(1, l):
                solve(i,j)
                if self.solved:
                    return True
        