class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        totSum=sum(nums)
        tar = totSum-target
        n=len(nums)
        if tar%2 or tar<0:
            return 0
        tar//=2
        dp = [0]*(tar+1)
        temp = [0]*(tar+1)
        if nums[0]==0:
            dp[0]=2
        else:
            dp[0]=1
        
        if nums[0]!=0 and nums[0]<=tar:
            dp[nums[0]]=1
             
        for i in range(1,n):
            for j in range(tar+1):
                y=0
                x=dp[j]
                if nums[i]<=j:
                    y=dp[j-nums[i]]
                     
                temp[j]=x+y
            dp=temp[:]
                 
        return dp[tar]