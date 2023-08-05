class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n=len(s)
        m=len(t)
        prev = [0]*m
        curr = [0]*m
        
        if s[0]==t[0]:
            prev[0]=1

        for i in range(1,n):
            for j in range(m):
                x=0
                if s[i]==t[j]:
                    if j>0:
                        x=prev[j-1]
                    else:
                        x=1

                y=prev[j]

                curr[j]=x+y
            prev=curr[:]

        return prev[m-1]