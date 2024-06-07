class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        visited = [False for i in nums]
        
        def permutations(current=[]):
            if len(current) == len(nums):
                perms.append(current.copy())
                return
            
            for ind, i in enumerate(nums):
                if visited[ind]:
                    continue
                
                current.append(i)
                visited[ind] = True
                permutations(current)
                visited[ind] = False
                current.pop()
                
        permutations()
        
        return perms