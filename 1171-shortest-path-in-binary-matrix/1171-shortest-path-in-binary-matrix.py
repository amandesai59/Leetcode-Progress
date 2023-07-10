class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0]:
            return -1

        n=len(grid)
        m=len(grid[0])
        if n==1 and m==1:
            return 1
        heap=[]
        heapq.heappush(heap, [1,[0,0]])

        while heap:
            dist, [x,y]=heapq.heappop(heap)
            
            for i in range(-1,2):
                for j in range(-1,2):
                    if (i or j) and x+i<n and x+i>=0 and y+j>=0 and y+j<m and grid[x+i][y+j]==0:
                        if x+i==n-1 and y+j==m-1:
                            return dist+1
                        heapq.heappush(heap, [dist+1,[x+i, y+j]])
                        grid[x+i][y+j]=1

        return -1