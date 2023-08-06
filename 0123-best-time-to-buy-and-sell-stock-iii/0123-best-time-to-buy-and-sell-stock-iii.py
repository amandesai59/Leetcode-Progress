class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        dp=[[[0]*(3) for _ in range(2)] for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(2):
                for k in range(1,3):
                    if j:
                        x = - prices[i] + dp[i+1][0][k]
                        y = dp[i+1][1][k]
                    else:
                        x = prices[i] + dp[i+1][1][k-1]
                        y = dp[i+1][0][k]

                    dp[i][j][k] = max(x,y)

        return dp[0][1][2]