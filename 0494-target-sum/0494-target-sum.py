class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        totSum=sum(nums)
        tar = totSum-target
        n=len(nums)
        if tar%2 or tar<0:
            return 0
        tar//=2
        dp = [[-1]*(tar+1) for _ in range(n)]
        return self.rec(nums, n-1, tar, dp)
            
    def rec(self, arr, i, tar, dp):
        
        if i==-1:
            return tar==0
            
        if dp[i][tar]!=-1:
            return dp[i][tar]
            
        y=0
        x=self.rec(arr, i-1, tar, dp)
        if arr[i]<=tar:
            y=self.rec(arr, i-1, tar-arr[i], dp)
        
        dp[i][tar]=x+y
        return x+y