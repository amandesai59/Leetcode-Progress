class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        ans=float('inf')
        n=len(matrix)
        dp=[[float('inf')]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i==0:
                    dp[i][j]=matrix[i][j]
                    continue
                x=float('inf')
                y=float('inf')

                if j>0:
                    x = dp[i-1][j-1]
                if j<n-1:
                    y = dp[i-1][j+1]
                z = dp[i-1][j]

                dp[i][j] = matrix[i][j] + min(x,y,z)

        return min(dp[-1])