class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        m=len(grid)
        n=len(grid[0])

        dp = [[-1e9]*n for _ in range(n)]

        dp[0][n-1] = grid[0][0] + grid[0][n-1]

        for x in range(1,m):
            temp = [[0]*n for _ in range(n)]
            for y1 in range(n):
                for y2 in range(n):
                    ans=-1e9
                    for i in range(-1,2):
                        for j in range(-1, 2):

                            p=y1+i
                            q=y2+j
                            if p>=0 and q>=0 and p<n and q<n:

                                curr = grid[x][y1] + dp[p][q]

                                if y1!=y2:
                                    curr += grid[x][y2]

                                ans = max(ans, curr)

                    temp[y1][y2]=ans
            
            dp=temp[:]

        return max(map(max, dp))