class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        s = 0
        e = 0
        for i in weights:
            e += i
            s = max(s, i)
        
        while s<e:
            mid = (s+e)//2
            ds = 1
            current = 0
            for i in weights:
                current += i
                if current>mid:
                    # print(current-i, i, ds)
                    current = i
                    ds += 1
                    
            # print(s,e,mid,ds)
                    
            if ds>days:
                s = mid+1
            else:
                e = mid
                
        return s
                
            
        