class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        ans=[[-1 for _ in range(m)] for _ in range(n)]
        visited=[[0 for _ in range(m)] for _ in range(n)]
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        zeros=[]

        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    zeros.append([i,j])
                    visited[i][j]=1
                    ans[i][j]=0

        queue=deque(zeros)
        dist=0
        while queue:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                if mat[i][j]==1 and ans[i][j]==-1:
                    ans[i][j]=dist
                for d in directions:
                    if self.valid(i+d[0],j+d[1],n,m) and visited[i+d[0]][j+d[1]]==0:
                        queue.append([i+d[0],j+d[1]])
                        visited[i+d[0]][j+d[1]]=1
            dist+=1

        return ans

    def valid(self, x, y, n, m):
        if x>=0 and x<n and y>=0 and y<m:
            return True
        return False