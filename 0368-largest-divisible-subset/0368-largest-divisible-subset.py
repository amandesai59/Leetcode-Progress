class Solution:
    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:

        n=len(arr)
        dp=[1]*(n)
        prev=[i for i in range(n)]
        maxx=0
        ind=0
        arr.sort()
        for i in range(n):
            for j in range(i):
                if arr[i]%arr[j]==0 and 1+dp[j]>dp[i]:
                    dp[i] = 1+dp[j]
                    prev[i]=j
                
                if dp[i]>maxx:
                    maxx=dp[i]
                    ind=i
        
        ans=[]
        while prev[ind]!=ind:
            ans.append(arr[ind])
            ind=prev[ind]
        ans.append(arr[ind])
        return ans[::-1]