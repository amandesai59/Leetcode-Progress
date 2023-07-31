class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        ans = self.rec(coins, amount, n-1, dp)

        if ans==float('inf'):
            return -1
        return ans
        
    def rec(self, coins, amount, i, dp):

        if amount==0:
            return 0
        
        if i<0:
            return float('inf')

        if dp[i][amount]!=-1:
            return dp[i][amount]

        n = amount//coins[i]

        x = self.rec(coins, amount, i-1, dp)
        y=float('inf')
        if coins[i]<=amount:
            y = 1+self.rec(coins, amount-coins[i], i, dp)

        dp[i][amount] = min(x,y)

        return dp[i][amount]