class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        m=len(grid)
        n=len(grid[0])

        dp = [[[-1e9]*n for _ in range(n)] for _ in range(m)]

        dp[0][0][n-1] = grid[0][0] + grid[0][n-1]

        for x in range(1,m):
            for y1 in range(n):
                for y2 in range(n):
                    ans=-1e9
                    for i in range(-1,2):
                        for j in range(-1, 2):

                            p=y1+i
                            q=y2+j
                            if p>=0 and q>=0 and p<n and q<n:

                                temp = grid[x][y1] + dp[x-1][y1+i][y2+j]

                                if y1!=y2:
                                    temp += grid[x][y2]

                                ans = max(ans, temp)

                    dp[x][y1][y2]=ans

        return max(map(max, dp[m-1]))