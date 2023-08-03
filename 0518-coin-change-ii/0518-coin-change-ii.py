class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        ans = self.rec(coins, amount, n-1, dp)

        return ans
        
    def rec(self, coins, amount, i, dp):

        if amount==0:
            return 1
        
        if i<0:
            return 0

        if dp[i][amount]!=-1:
            return dp[i][amount]

        n = amount//coins[i]

        x = self.rec(coins, amount, i-1, dp)
        y=0
        if coins[i]<=amount:
            y = self.rec(coins, amount-coins[i], i, dp)

        dp[i][amount] = x+y

        return dp[i][amount]
