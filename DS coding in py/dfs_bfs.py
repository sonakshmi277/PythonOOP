from collections import deque
adj = [[2, 3, 1], [0], [0, 4], [0, 4], [2]]
class Solution:
    # DFS Traversal from vertex 0
    def dfsOfGraph(self, V, adj):
        visited = [False] * V
        result = []

        def dfs(node):
            visited[node] = True
            result.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        dfs(0)
        return result

    # BFS Traversal from vertex 0
    def bfsOfGraph(self, V, adj):
        visited = [False] * V
        result = []
        queue = deque()

        queue.append(0)
        visited[0] = True

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result

# Sample Input
V = 5
adj = [[2, 3, 1], [0], [0, 4], [0, 4], [2]]

sol = Solution()
print("DFS:", sol.dfsOfGraph(V, adj))   # Output: [0, 2, 4, 3, 1]
print("BFS:", sol.bfsOfGraph(V, adj))   # Output: [0, 2, 3, 1, 4]
