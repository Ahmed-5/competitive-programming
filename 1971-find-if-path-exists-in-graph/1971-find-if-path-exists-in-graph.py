class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        visited = [False for i in range(n)]
        
        g = []
        for i in range(n):
            g.append([])
        
        for e in edges:
            i,j = e[0], e[1]
            g[i].append(j)
            g[j].append(i)
        
        def dfs(source, destination):
            if visited[source]:
                return False
            
            if source==destination:
                return True
            
            visited[source]=True
            for i in g[source]:
                if dfs(i, destination):
                    return True
                
            return False
        

        return dfs(source, destination)