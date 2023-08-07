class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n=len(nums)
        dp=[1]*(n)
        count=[1]*(n)
        maxx=0

        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    if 1+dp[j] > dp[i]:
                        dp[i] =1+dp[j]
                        count[i] = count[j]
                    elif 1+dp[j] == dp[i]:
                        count[i] += count[j]
            maxx=max(maxx, dp[i])

        ans=0
        for i in range(n):
            if dp[i]==maxx:
                ans+=count[i]

        return ans