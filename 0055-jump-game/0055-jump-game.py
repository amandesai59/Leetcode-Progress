class Solution:
    def canJump(self, nums: List[int]) -> bool:

        maxReach=nums[0]

        for i in range(1,len(nums)):
            if maxReach<i:
                return False
            if nums[i]+i > maxReach:
                maxReach=nums[i]+i

        return True