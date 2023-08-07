class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n=len(nums)
        arr=[nums[0]]

        for i in range(1,n):
            if nums[i]>arr[-1]:
                arr.append(nums[i])
            else:
                lower = bisect.bisect_left(arr, nums[i])
                arr[lower]=nums[i]
            
        return len(arr)