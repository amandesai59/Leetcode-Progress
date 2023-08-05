class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n=len(s)
        dp = [[-1]*n for _ in range(n)]
        return self.rec(s, s[::-1], n-1, n-1, dp)

    def rec(self, text1, text2, i, j, dp):

        if i==0 and j==0:
            if text1[0] == text2[0]:
                return 1
            return 0

        if dp[i][j]!=-1:
            return dp[i][j]
        x=0
        y=0
        z=0

        if text1[i] == text2[j]:
            if i==0 or j==0:
                x=1
            else:
                x = 1 + self.rec(text1, text2, i-1, j-1, dp)

        else:
            if i>0:
                y=self.rec(text1,text2, i-1, j, dp)
            if j>0:
                z=self.rec(text1, text2, i, j-1, dp)

        dp[i][j] = max(x,y,z)
        return dp[i][j]