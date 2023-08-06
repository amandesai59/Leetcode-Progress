class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        dp=[[[-1]*(3) for _ in range(2)] for _ in range(n)]
        return self.rec(prices, n, 0, 2, 1, dp)

    def rec(self, prices, n, i, cap, buy, dp):

        if i==n or cap==0:
            return 0

        if dp[i][buy][cap]!=-1:
            return dp[i][buy][cap]

        if buy:
            x = - prices[i] + self.rec(prices, n, i+1, cap, 0, dp)
            y = self.rec(prices, n, i+1, cap, 1, dp)
        else:
            x = prices[i] + self.rec(prices, n, i+1, cap-1, 1, dp)
            y = self.rec(prices, n, i+1, cap, 0, dp)

        dp[i][buy][cap] = max(x,y)
        return max(x,y)