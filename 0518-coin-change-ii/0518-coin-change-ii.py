class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n)]

        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=1
            else:
                dp[0][i]=0

        for i in range(1,n):
            for j in range(amount+1):
                x = dp[i-1][j]
                y=0
                if coins[i]<=j:
                    y = dp[i][j-coins[i]]

                dp[i][j] = x+y

        return dp[n-1][amount]