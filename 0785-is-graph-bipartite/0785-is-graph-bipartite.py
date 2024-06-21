class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [None for i in graph]
        g = graph
        isVisited = [False for i in graph]
            
            
        for i in range(n):
            if not isVisited[i]:
                cc = None
                for j in g[i]:
                    if cc is not None and colors[j] == cc:
                        return False
                    if cc is None and colors[j] is not None:
                        cc = not colors[j]
                        
                if cc is None:
                    cc = True
                stack = [(i, cc)]
                
                while len(stack) != 0:
                    node, color = stack.pop()
                    if isVisited[node]:
                        continue
                    colors[node] = color
                    for new_node in g[node]:
                        if colors[new_node] is None:
                            stack.append((new_node, not color))
                        elif colors[new_node] == color:
                            return False
                        
                    isVisited[node] = True
                        
        return True