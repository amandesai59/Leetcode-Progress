class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n=len(matrix)
        m=len(matrix[0])
        first=1

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    if j==0:
                        first=0
                    else:
                        matrix[0][j]=0
                        matrix[i][0]=0


        for i in range(n-1,-1,-1):
            for j in range(1,m):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            if first==0:
                matrix[i][0]=0