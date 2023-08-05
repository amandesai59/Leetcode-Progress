class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n=len(word1)
        m=len(word2)

        if n<m:
            dp = [[-1]*n for _ in range(m)]
            return self.rec(word2, word1, m-1, n-1, dp)

        dp = [[-1]*m for _ in range(n)]
        return self.rec(word1, word2, n-1, m-1, dp)

    def rec(self, word1, word2, i, j, dp):

        if j<0:
            return i+1

        if i<0:
            return j+1

        if dp[i][j]!=-1:
            return dp[i][j]

        x=float('inf')
        y=float('inf')
        z=float('inf')

        if word1[i]==word2[j]:
            x=self.rec(word1, word2, i-1, j-1, dp)
        else:
            x=1+self.rec(word1, word2, i, j-1, dp)
            y=1+self.rec(word1, word2, i-1, j-1, dp)
            z=1+self.rec(word1, word2, i-1,j, dp)

        dp[i][j]=min(x,y,z)
        return dp[i][j]