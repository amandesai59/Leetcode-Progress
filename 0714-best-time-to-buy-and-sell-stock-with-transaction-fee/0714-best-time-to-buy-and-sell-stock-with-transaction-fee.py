class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n=len(prices)
        curr=[0,0]
        after=[0,0]
        
        for i in range(n-1, -1, -1):

            curr[1] = max(-prices[i] + after[0], after[1])
            curr[0] = max(prices[i] -fee + after[1], after[0])
            after=curr[:]

        return after[1]