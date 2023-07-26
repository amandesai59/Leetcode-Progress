class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        ans=float('inf')
        n=len(matrix)
        dp=[float('inf')]*n

        for i in range(n):
            temp=[0]*n
            for j in range(n):
                if i==0:
                    temp[j]=matrix[i][j]
                    continue
                x=float('inf')
                y=float('inf')

                if j>0:
                    x = dp[j-1]
                if j<n-1:
                    y = dp[j+1]
                z = dp[j]

                temp[j] = matrix[i][j] + min(x,y,z)
            dp=temp[:]

        return min(dp)