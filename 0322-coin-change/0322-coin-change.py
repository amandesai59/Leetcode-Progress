class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n)]

        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=i//coins[0]
            else:
                dp[0][i]=float('inf')

        for i in range(1,n):
            for j in range(amount+1):
                x = dp[i-1][j]
                y=float('inf')
                if coins[i]<=j:
                    y = 1+dp[i][j-coins[i]]

                dp[i][j] = min(x,y)

        ans = dp[n-1][amount]
        if ans==float('inf'):
            return -1
        return ans