class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        dp=[[-1]*(4) for _ in range(n)]
        return self.rec(prices, n, 0, 0, dp)

    def rec(self, prices, n, i, trNo, dp):

        if i==n or trNo==4:
            return 0

        if dp[i][trNo]!=-1:
            return dp[i][trNo]

        if trNo%2==0:
            x = - prices[i] + self.rec(prices, n, i+1, trNo+1, dp)
            y = self.rec(prices, n, i+1, trNo, dp)
        else:
            x = prices[i] + self.rec(prices, n, i+1, trNo+1, dp)
            y = self.rec(prices, n, i+1, trNo, dp)

        dp[i][trNo] = max(x,y)
        return max(x,y)