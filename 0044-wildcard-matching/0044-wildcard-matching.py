class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n=len(s)
        m=len(p)
        dp=[[-1]*m for _ in range(n)]
        return self.rec(s,p,n-1, m-1, dp)

    def rec(self, s, p, i, j, dp):

        if i<0:
            while j>=0 and p[j]=='*':
                j-=1
            if j<0:
                return True
            return False

        if j<0:
            return False

        if dp[i][j]!=-1:
            return dp[i][j]

        ans=False
        if s[i]==p[j] or p[j]=='?':
            ans = self.rec(s, p, i-1, j-1, dp)
        elif p[j]=='*':
            x = self.rec(s,p,i-1,j, dp)
            y = self.rec(s,p,i-1,j-1, dp)
            z = self.rec(s,p,i,j-1, dp)
            ans = x or y or z
        
        dp[i][j] = ans
        return ans