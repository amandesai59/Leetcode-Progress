class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        n=len(g)
        m=len(s)
        i=0
        j=0
        ans=0

        while i<n and  j<m:
            if g[i]<=s[j]:
                ans+=1
                i+=1
            j+=1
        return ans