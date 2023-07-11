class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        matrix=[[float('inf') for _ in range(n)] for _ in range(n)]

        for i,j,w in edges:
            matrix[i][j]=w
            matrix[j][i]=w

        for i in range(n):
            matrix[i][i]=0

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][via]==float('inf') or matrix[via][j]==float('inf'):
                        continue
                    matrix[i][j] = min(matrix[i][j], matrix[i][via] + matrix[via][j])

        ans=n+1
        node=-1
        for i in range(n):
            curr=0
            for j in range(n):
                if matrix[i][j]<=distanceThreshold:
                    curr+=1
            if curr<=ans:
                ans=curr
                node=i

        return node