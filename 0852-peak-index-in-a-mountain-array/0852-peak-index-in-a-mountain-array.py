class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s = 0
        e = len(arr)-1
        
        if arr[0]>arr[1]:
            return 0
        
        if arr[-1]>arr[-2]:
            return e
        
        while s<=e:
            mid = int((s+e)//2)
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]<arr[mid]:
                s = mid+1
            else:
                e = mid-1
                
        return min(max(mid, 1), len(arr)-2)
            
            