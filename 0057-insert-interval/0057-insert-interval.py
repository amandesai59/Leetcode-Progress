class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ans=[]

        if not intervals:
            return [newInterval]

        for interval in intervals:
            if newInterval:
                if newInterval[0]>=interval[0] and newInterval[0]<=interval[1]:
                    interval[1]=max(newInterval[1], interval[1])
                    newInterval=None
                elif newInterval[1]>=interval[0] and newInterval[1]<=interval[1]:
                    interval[0]=min(newInterval[0],interval[0])
                    newInterval=None
                elif newInterval[0]<=interval[0] and newInterval[1]>=interval[1]:
                    interval=newInterval
                    newInterval=None
                elif newInterval[0]<interval[0]:
                    ans.append(newInterval)
                    newInterval=None
            elif ans and interval[0]>=ans[-1][0] and interval[0]<=ans[-1][1]:
                temp=ans.pop()
                interval=[temp[0], max(temp[1],interval[1])]
            ans.append(interval)
        if newInterval:
            ans.append(newInterval)
        return ans