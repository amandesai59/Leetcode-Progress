class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key=lambda x: len(x))
        n=len(words)
        dp=[1]*(n)

        for i in range(n):
            for j in range(i):
                if self.check(words[i], words[j]):
                    dp[i] = max(1+dp[j], dp[i])

        return max(dp)

    def check(self, curr, prev):

        n=len(curr)
        m=len(prev)

        if n!=m+1:
            return False

        count=0
        i=0
        j=0

        while i<n and j<m:
            if curr[i]!=prev[j]:
                count+=1
                if count>1:
                    return False
                i+=1
            else:
                i+=1
                j+=1
        
        if count==1 and i!=n:
            return False
        return True