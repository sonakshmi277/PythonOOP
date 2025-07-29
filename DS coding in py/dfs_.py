class Solution:
    def ans(self,V,adj):
        visited=[0]*V
        ans=[]
        def dfs(node):
            ans.append(node)
            visited[node]=True
            for nodes in adj[node]:
                if not visited[nodes]:
                    dfs(nodes)
            
        dfs(0) 
        return ans 
obj=Solution()
print(obj.ans(5,[[2, 3, 1], [0], [0, 4], [0, 4], [2]]))

