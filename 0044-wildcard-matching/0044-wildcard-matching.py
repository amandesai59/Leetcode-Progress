class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n=len(s)
        m=len(p)
        dp=[[False]*(m+1) for _ in range(n+1)]
        dp[0][0]=True
        for j in range(m):
            if p[j]=='*':
                dp[0][j+1]=True
            else:
                break

        for i in range(1, n+1):
            for j in range(1, m+1):
                ans=False
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[n][m]