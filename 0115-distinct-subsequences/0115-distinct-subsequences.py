class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n=len(s)
        m=len(t)
        curr = [0]*m
        
        if s[0]==t[0]:
            curr[0]=1

        for i in range(1,n):
            for j in range(m-1,-1,-1):
                x=0
                if s[i]==t[j]:
                    if j>0:
                        x=curr[j-1]
                    else:
                        x=1

                curr[j]+=x

        return curr[-1]