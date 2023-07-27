class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        m=len(grid)
        n=len(grid[0])

        dp = [[[-1]*n for _ in range(n)] for _ in range(m)]

        return self.rec(grid, 0, 0, n-1, m, n, dp)

        
    def rec(self, grid, x, y1, y2, m, n, dp):

        if y1<0 or y2<0 or y1>=n or y2>=n:
            return -1e9

        if dp[x][y1][y2]!=-1:
            return dp[x][y1][y2]

        if x==m-1:
            if y1!=y2:
                return grid[x][y1] + grid[x][y2]
            return grid[x][y1]
        
        ans=-1e9

        for i in range(-1,2):
            for j in range(-1, 2):
                temp = grid[x][y1] + self.rec(grid, x+1, y1+i, y2+j, m, n, dp)

                if y1!=y2:
                    temp += grid[x][y2]

                ans = max(ans, temp)

        dp[x][y1][y2]=ans
        return ans