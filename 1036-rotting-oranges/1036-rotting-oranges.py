class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans=0
        n=len(grid)
        m=len(grid[0])
        visited=[[0 for i in range(m)] for _ in range(n)]
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        rottens=[]

        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    visited[i][j]=1
                    rottens.append([i,j])

        ans=self.bfs(grid, rottens, n, m, directions, visited)

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1

        return ans

    def bfs(self, grid, rotten, n, m, directions, visited):
        queue=deque(rotten)
        currAns=0
        while queue:
            for _ in range(len(queue)):
                i,j=queue.popleft()

                for d in directions:
                    if self.valid(i+d[0],j+d[1],n,m) and grid[i+d[0]][j+d[1]]==1:
                        grid[i+d[0]][j+d[1]]=2
                        queue.append([i+d[0],j+d[1]])
                        visited[i+d[0]][j+d[1]]=1
            if queue:
                currAns+=1
        return currAns


    def valid(self, x, y, n, m):
        if x>=0 and x<n and y>=0 and y<m:
            return True
        return False