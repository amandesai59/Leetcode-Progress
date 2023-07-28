class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        totSum=sum(nums)
        if totSum%2:
            return False

        return self.isSubsetSum(len(nums), nums, totSum//2)


    def isSubsetSum(self, N, arr, target):
        
        dp = [False]*(max(100, target)+1)
        dp[0]=True
            
        dp[arr[0]]=True
        
        for i in range(1, N):
            temp = [False]*(max(100, target)+1)
            temp[0]=True
            for j in range(1, target+1):
                x = dp[j]
                y=False
                if j-arr[i] >= 0:
                    y = dp[j-arr[i]]
                temp[j] = x or y
            dp=temp[:]
        return dp[target]