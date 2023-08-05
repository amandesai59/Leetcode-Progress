class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n=len(s)
        prev = [0]*(n+1)
        curr = [0]*(n+1)
        text1=s
        text2=s[::-1]

        for i in range(1,n+1):
            for j in range(1,n+1):
                x=0
                y=0
                z=0

                if text1[i-1] == text2[j-1]:
                    x = 1 + prev[j-1]

                else:
                    y=prev[j]
                    z=curr[j-1]

                curr[j] = max(x,y,z)
            prev=curr[:]
            
        return prev[n]