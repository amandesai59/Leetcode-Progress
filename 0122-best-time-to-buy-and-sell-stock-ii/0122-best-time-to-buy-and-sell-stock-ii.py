class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        currMin=prices[0]
        ans=0

        for i in range(1, len(prices)):

            if prices[i]<prices[i-1]:
                ans+=prices[i-1]-currMin
                currMin=prices[i]

        ans+=prices[-1]-currMin
        return ans