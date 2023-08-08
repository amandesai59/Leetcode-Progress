class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n=len(matrix)
        m=len(matrix[0])
        first=1
        row=[1]*n
        column=[1]*m

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row[i]=0
                    column[j]=0

        for i in range(n):
            if row[i]==0:
                for j in range(m):
                    matrix[i][j]=0

        print(row)
        print(column)

        for j in range(m):
            if column[j]==0:
                for i in range(n):
                    matrix[i][j]=0            