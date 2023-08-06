class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        n=len(prices)
        curr=[0]*(k*2+1)
        after=[0]*(k*2+1)

        for i in range(n-1, -1, -1):
            for j in range(k*2-1, -1,-1):
                if j%2==0:
                    x = - prices[i] + after[j+1]
                    y = after[j]
                else:
                    x = prices[i] + after[j+1]
                    y = after[j]

                curr[j] = max(x,y)
            after=curr[:]

        return curr[0]
