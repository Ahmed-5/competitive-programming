class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        s1 = set(arr1)
        s2 = set(arr2)
        sd = s1 - s2
        sd = list(sd)
        sd.sort()
        count = [0 for i in range(1001)]
        l = []
        
        for i in arr1:
            count[i] += 1
            
        for i in arr2:
            v = count[i]
            for _ in range(v):
                l.append(i)
            
        for i in sd:
            v = count[i]
            for _ in range(v):
                l.append(i)
                
        return l