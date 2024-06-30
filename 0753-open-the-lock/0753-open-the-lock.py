from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = [False for i in range(10000)]
        for i in deadends:
            visited[int(i)] = True
        
        def get_options(comb, steps):
            c = [int(i) for i in comb]
            l = []
            for i in range(4):
                c[i] = (c[i]+1)%10
                sc = [str(i) for i in c]
                sc = "".join(sc)
                if not visited[int(sc)]:
                    l.append([sc, steps+1])
                c[i] = (c[i]-1)%10

                
                c[i] = (c[i]-1)%10
                sc = [str(i) for i in c]
                sc = "".join(sc)
                if not visited[int(sc)]:
                    l.append([sc, steps+1])
                c[i] = (c[i]+1)%10

            return l

        q = deque([["0000", 0]])
        while len(q)>0:
            c, s = q.popleft()
            ci = int(c)
            if visited[ci]:
                continue

            if c == target:
                return s

            visited[ci] = True

            cs = get_options(c, s)
            for i in cs:
                q.append(i)

        return -1