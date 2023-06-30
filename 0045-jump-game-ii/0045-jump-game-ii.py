class Solution:
    def jump(self, nums: List[int]) -> int:

        ans=0
        n=len(nums)
        maxReach=0
        i=0

        while maxReach<n-1:
            currReach=maxReach
            for j in range(i,currReach+1):
                maxReach=max(maxReach, nums[j]+j)
            ans+=1
            i=currReach

        return ans