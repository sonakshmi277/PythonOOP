from collections import deque
class Solution:
    def bfs(self,V,adj):
        visited=[0]*V
        visited[0]=True
        q=deque()
        q.append(0)
        result=[]
        while q:
            node=q.popleft()
            result.append(node)
            for nodes in adj[node]:
                if not visited[nodes]:
                    visited[nodes]=True
                    q.append(nodes)
        return result

obj=Solution()
print(obj.bfs(5,[[2, 3, 1], [0], [0, 4], [0, 4], [2]]))
