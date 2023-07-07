class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        V=len(graph)
        visited=[0]*V
        ans=set()

        for i in range(V):
            if not visited[i]:
                self.dfs(graph, i, visited, ans)

        return sorted(list(ans))

    def dfs(self, graph, x, visited, ans):

        visited[x]=1

        if not graph[x]:
            ans.add(x)
            return True

        for i in graph[x]:
            if not visited[i]:
                if not self.dfs(graph, i, visited, ans):
                    return False
            elif i not in ans:
                return False

        ans.add(x)
        return True