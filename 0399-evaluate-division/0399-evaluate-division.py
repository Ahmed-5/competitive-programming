from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(lambda: defaultdict(lambda: -1.0))
        
        for eq, v in zip(equations, values):
            var1, var2 = eq
            graph[var1][var2] = 1.0*v
            graph[var2][var1] = 1.0/v
            
        def dfs(source, dest):
            if source not in graph or dest not in graph:
                return -1.0
            
            if source==dest:
                return 1.0
            
            visited[source] = True
            
            for new_source in graph[source]:
                if not visited[new_source]:
                    ans = dfs(new_source, dest)
                    if ans != -1:
                        return graph[source][new_source] * ans
            
            return -1
            
        answers = []
        for s, d in queries:
            visited = defaultdict(lambda: False)
            ans = dfs(s,d)
            answers.append(ans)
            
        return answers