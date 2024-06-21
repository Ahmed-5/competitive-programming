from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(lambda: defaultdict(lambda: -1.0))
        
        for eq, v in zip(equations, values):
            var1, var2 = eq
            graph[var1][var2] = 1.0*v
            graph[var2][var1] = 1.0/v
            
        def dfs(source, dest):
            # print("DFS")
            visited = defaultdict(lambda: False)
            if source not in graph or dest not in graph:
                return -1.0
            
            if source==dest:
                return 1.0
            
            stack = [[source, dest, 1]]
            while len(stack)>0:
                s, d, v = stack.pop()
            
                visited[s] = True
                if s==d:
                    return v
                
                for i in graph[s]:
                    if visited[i]:
                        continue
                        
                    stack.append([i, d, v*graph[s][i]])
            
            return -1
            
        answers = []
        for s, d in queries:
            ans = dfs(s,d)
            answers.append(ans)
            
        return answers