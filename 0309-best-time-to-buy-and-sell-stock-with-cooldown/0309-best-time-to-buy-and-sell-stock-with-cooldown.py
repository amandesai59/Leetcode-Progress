class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        curr=[[0]*2 for _ in range(2)]
        after=[[0]*2 for _ in range(2)]

        for i in range(n-1, -1, -1):
            for j in range(2):
                curr[j][1] = after[1][0]

                if j:
                    x = -prices[i] + after[0][0]
                    y = after[1][0]
                else:
                    x = prices[i] + after[1][1]
                    y = after[0][0]

                curr[j][0]=max(x,y)
            after=curr[:]

        return curr[1][0]