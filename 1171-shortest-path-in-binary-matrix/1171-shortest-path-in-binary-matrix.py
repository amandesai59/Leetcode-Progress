class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0]:
            return -1

        n=len(grid)
        if n==1:
            return 1
        queue=deque([[1,0,0]])

        while queue:
            dist, x, y=queue.popleft()
            
            for i in range(-1,2):
                for j in range(-1,2):
                    if (i or j) and x+i<n and x+i>=0 and y+j>=0 and y+j<n and grid[x+i][y+j]==0:
                        if x+i==n-1 and y+j==n-1:
                            return dist+1
                        queue.append([dist+1, x+i, y+j])
                        grid[x+i][y+j]=1

        return -1