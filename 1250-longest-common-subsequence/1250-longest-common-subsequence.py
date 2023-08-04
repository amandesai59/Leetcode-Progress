class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n=len(text1)
        m=len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n):
            dp[i][0]=0
        for j in range(m):
            dp[0][j]=0

        for i in range(1,n+1):
            for j in range(1,m+1):
                x=0
                y=0
                z=0

                if text1[i-1] == text2[j-1]:
                    x = 1 + dp[i-1][j-1]

                else:
                    y=dp[i-1][j]
                    z=dp[i][j-1]

                dp[i][j] = max(x,y,z)
            
        return dp[n][m]