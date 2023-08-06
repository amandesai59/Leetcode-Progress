class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        curr=[[0]*(3) for _ in range(2)]
        after=[[0]*(3) for _ in range(2)]

        for i in range(n-1, -1, -1):
            for j in range(2):
                for k in range(1,3):
                    if j:
                        x = - prices[i] + after[0][k]
                        y = after[1][k]
                    else:
                        x = prices[i] + after[1][k-1]
                        y = after[0][k]

                    curr[j][k] = max(x,y)
            after=curr[:]

        return curr[1][2]