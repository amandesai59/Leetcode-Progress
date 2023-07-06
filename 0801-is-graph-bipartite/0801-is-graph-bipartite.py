class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        partisan={}
        n=len(graph)
        for i in range(n):
            if i not in partisan:
                if not self.dfs(graph, i, partisan, -1):
                    return False
        
        return True
        
    def dfs(self, graph, x, partisan, parent):

        partisan[x]=-parent

        for i in graph[x]:
            if (i not in partisan) and (not self.dfs(graph, i, partisan, -parent)):
                return False
            elif i in partisan and partisan[i]==-parent:
                return False

        return True
                