class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n=len(s)
        m=len(t)
        dp=[[0]*m for _ in range(n)]
        
        if s[0]==t[0]:
            dp[0][0]=1

        for i in range(1,n):
            for j in range(m):
                x=0
                if s[i]==t[j]:
                    if j>0:
                        x=dp[i-1][j-1]
                    else:
                        x=1

                y=dp[i-1][j]

                dp[i][j]=x+y

        return dp[n-1][m-1]