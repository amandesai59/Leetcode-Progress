class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        dp=[[[-1]*2 for _ in range(2)] for _ in range(n)]
        return self.rec(prices, n, 0, 1, 0, dp)

    def rec(self, prices, n, i, buy, cool, dp):

        if i==n:
            return 0

        if dp[i][buy][cool]!=-1:
            return dp[i][buy][cool]

        if cool:
            return self.rec(prices, n, i+1, buy, 0, dp)

        if buy:
            x = -prices[i] + self.rec(prices, n, i+1, 0, 0, dp)
            y = self.rec(prices, n, i+1, 1, 0, dp)
        else:
            x = prices[i] + self.rec(prices, n, i+1, 1, 1, dp)
            y = self.rec(prices, n, i+1, 0, 0, dp)

        dp[i][buy][cool]=max(x,y)
        return max(x,y)