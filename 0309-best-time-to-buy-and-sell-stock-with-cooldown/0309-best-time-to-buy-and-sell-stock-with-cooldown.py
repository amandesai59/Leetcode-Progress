class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        dp=[[[0]*2 for _ in range(2)] for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(2):
                dp[i][j][1] = dp[i+1][1][0]

                if j:
                    x = -prices[i] + dp[i+1][0][0]
                    y = dp[i+1][1][0]
                else:
                    x = prices[i] + dp[i+1][1][1]
                    y = dp[i+1][0][0]

                dp[i][j][0]=max(x,y)

        return dp[0][1][0]