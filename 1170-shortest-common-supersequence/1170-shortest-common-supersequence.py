class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:

        n=len(s1)
        m=len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                x=0
                y=0
                z=0

                if s1[i-1] == s2[j-1]:
                    x = 1 + dp[i-1][j-1]

                else:
                    y=dp[i-1][j]
                    z=dp[i][j-1]

                dp[i][j] = max(x,y,z)

        i=n
        j=m
        curr=dp[i][j]-1

        ans=''

        while i>0 and j>0:
            if s1[i-1]==s2[j-1]:
                ans=s1[i-1]+ans
                i-=1
                j-=1
            elif dp[i-1][j] > dp[i][j-1]:
                ans=s1[i-1]+ans
                i-=1
            else:
                ans=s2[j-1]+ans
                j-=1

        while i>0:
            ans=s1[i-1]+ans
            i-=1

        while j>0:
            ans=s2[j-1]+ans
            j-=1


        return ans