class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        dp=[[0]*(5) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(3, -1,-1):
                if j%2==0:
                    x = - prices[i] + dp[i+1][j+1]
                    y = dp[i+1][j]
                else:
                    x = prices[i] + dp[i+1][j+1]
                    y = dp[i+1][j]

                dp[i][j] = max(x,y)

        return dp[0][0]