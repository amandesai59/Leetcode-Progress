class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        return self.rec(prices, n, 0, 1, fee, dp)
    
    def rec(self, prices, n, i, buy, fee, dp):

        if i==n:
            return 0

        if dp[i][buy]!=-1:
            return dp[i][buy]

        if buy:
            x = -prices[i] + self.rec(prices, n, i+1, 0, fee, dp)
            y = self.rec(prices, n, i+1, 1, fee, dp)
        else:
            x = prices[i] - fee + self.rec(prices, n, i+1, 1, fee ,dp)
            y = self.rec(prices, n, i+1, 0, fee, dp)

        dp[i][buy] = max(x,y)
        return dp[i][buy]