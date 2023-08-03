class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        prev = [0]*(amount+1)
        curr = [0]*(amount+1)

        for i in range(amount+1):
            if i%coins[0]==0:
                prev[i]=1
            else:
                prev[i]=0

        for i in range(1,n):
            for j in range(amount+1):
                x = prev[j]
                y=0
                if coins[i]<=j:
                    y = curr[j-coins[i]]

                curr[j] = x+y
            prev=curr[:]

        return prev[amount]