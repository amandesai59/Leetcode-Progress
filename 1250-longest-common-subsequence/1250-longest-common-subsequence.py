class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n=len(text1)
        m=len(text2)
        dp = [[-1]*m for _ in range(n)]

        return self.rec(text1, text2, len(text1)-1, len(text2)-1, dp)

    def rec(self, text1, text2, i, j, dp):

        if (i==0 or j==0) and text1[i] == text2[j]:
            return 1

        if dp[i][j]!=-1:
            return dp[i][j]
        x=0
        y=0
        z=0

        if text1[i] == text2[j]:
            x = 1 + self.rec(text1, text2, i-1, j-1, dp)

        else:
            if i>0:
                y=self.rec(text1,text2, i-1, j, dp)
            if j>0:
                z=self.rec(text1, text2, i, j-1, dp)

        dp[i][j] = max(x,y,z)
        return dp[i][j]