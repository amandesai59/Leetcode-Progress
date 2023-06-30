class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[1])
        j=1
        ans=0
            
        for i in range(1, len(intervals)):
            
            if (intervals[i][0] < intervals[i-j][1]):
                j+=1
                ans+=1
            else:
                j=1
                
        return ans