class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex
        arr = [1]
        s = n
        mul = 1
        e = 1
        
        while e<=n:
            mul = int(mul*s/e)
            arr.append(mul)
            e += 1
            s -= 1
            
        return arr
        