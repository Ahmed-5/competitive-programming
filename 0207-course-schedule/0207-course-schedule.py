class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        visited = [0 for i in range(numCourses)]
        
        for i, j in prerequisites:
            graph[i].append(j)
            
        def dfs(source):
            visited[source] = 1
            
            for new_source in graph[source]:
                if visited[new_source] == 1:
                    return False
                if visited[new_source] == 0:
                    if not dfs(new_source):
                        return False
                    
            visited[source] = 2
            
            return True
        
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True