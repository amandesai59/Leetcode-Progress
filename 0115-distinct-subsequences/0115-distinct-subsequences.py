class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n=len(s)
        m=len(t)
        dp=[[-1]*m for _ in range(n)]
        return self.rec(s,t,n-1, m-1, dp)

    def rec(self, s, t, i, j, dp):

        if i==0:
            if j==0 and s[0]==t[0]:
                return 1
            return 0

        if dp[i][j]!=-1:
            return dp[i][j]
        x=0
        if s[i]==t[j]:
            if j>0:
                x=self.rec(s,t,i-1,j-1, dp)
            else:
                x=1

        y=self.rec(s,t,i-1,j, dp)

        dp[i][j]=x+y
        return x+y