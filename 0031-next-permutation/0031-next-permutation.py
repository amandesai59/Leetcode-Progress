class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n==1:
            return

        for i in range(n-1,0,-1):
            if nums[i]>nums[i-1]:
                break

        i-=1
        if i>=0:
            for j in range(n-1, i, -1):
                if nums[i]<nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    nums[i+1:]=nums[:i:-1]
                    return
        
        nums[:]=nums[::-1]
        return