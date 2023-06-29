class Solution:
    def checkValidString(self, s: str) -> bool:
        openPar=0
        stars=0
        usedStars=0

        for i in s:
            if i=='(':
                openPar+=1
            elif i=='*':
                if openPar:
                    usedStars+=1
                    openPar-=1
                else:
                    stars+=1
            else:
                if openPar:
                    openPar-=1
                elif stars:
                    stars-=1
                elif usedStars:
                    usedStars-=1
                    stars+=1
                else:
                    return False

        if openPar:
            return False
        return True