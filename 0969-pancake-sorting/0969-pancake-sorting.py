class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        l = [i for i in arr]
        l.sort()
        
        n = len(l)-1
        swaps = []
        
        while n >= 0:
            target = l.pop()
            ind = arr.index(target)
            if ind == n:
                pass
            elif ind == 0:
                swaps.append(n+1)
                
                n2 = int((n+1)//2)
                for i in range(n2):
                    r = n-i
                    arr[r], arr[i] = arr[i], arr[r]
            else:
                swaps.append(ind+1)
                swaps.append(n+1)
                
                ind2 = int((ind+1)//2)
                for i in range(ind2):
                    r = ind-i
                    arr[r], arr[i] = arr[i], arr[r]
                
                n2 = int((n+1)//2)
                for i in range(n2):
                    r = n-i
                    arr[r], arr[i] = arr[i], arr[r]
                
            n -= 1
        return swaps