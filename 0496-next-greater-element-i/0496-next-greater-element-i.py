class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {i:-1 for i in nums1}
        l = []
        
        for i in nums2:
            while len(l)>0 and i>l[-1]:
                x = l.pop()
                d[x] = i
            if i in d and d[i]==-1:
                l.append(i)
        
        res = [d[i] for i in d]
        
        return res