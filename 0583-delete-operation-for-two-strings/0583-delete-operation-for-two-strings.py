class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n=len(word1)
        m=len(word2)
        prev = [0]*(m+1)
        curr = [0]*(m+1)

        for i in range(1,n+1):
            for j in range(1,m+1):
                x=0
                y=0
                z=0

                if word1[i-1] == word2[j-1]:
                    x = 1 + prev[j-1]

                else:
                    y=prev[j]
                    z=curr[j-1]

                curr[j] = max(x,y,z)
            prev=curr[:]
            
        return n+m-2*prev[m]