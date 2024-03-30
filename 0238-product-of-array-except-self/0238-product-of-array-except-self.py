class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        pre_prod = 1
        suf_prod = 1
        n = len(nums)
        
        for i in range(n):
            pre_prod *= nums[i]
            suf_prod *= nums[-i-1]
            prefix.append(pre_prod)
            suffix.append(suf_prod)
            
        prods = []
        
        for i in range(n):
            p = prefix[i]*suffix[-i-2]
            prods.append(p)
            
        return prods