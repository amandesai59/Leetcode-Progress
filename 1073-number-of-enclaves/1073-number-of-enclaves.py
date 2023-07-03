class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])

        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        for i in range(n):
            if grid[i][0]:
                self.dfs(grid, i, 0, n, m, directions)

            if grid[i][m-1]:
                self.dfs(grid, i, m-1, n, m, directions)

        for j in range(m):
            if grid[0][j]:
                self.dfs(grid, 0, j, n, m, directions)

            if grid[n-1][j]:
                self.dfs(grid, n-1, j, n, m, directions)

        ans=0
        for i in range(1,n-1):
            for j in range(1,m-1):
                if grid[i][j]:
                    ans+=1

        return ans

    def dfs(self, grid, x, y, n, m, directions):
        grid[x][y]=0
        for d in directions:
            i=x+d[0]
            j=y+d[1]

            if i>=0 and j>=0 and i<n and j<m and grid[i][j]:
                self.dfs(grid, i, j, n, m, directions)