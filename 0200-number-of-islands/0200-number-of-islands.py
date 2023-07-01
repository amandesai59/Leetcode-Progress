class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j]=='1':
                    grid[i][j]='0'
                    self.removeIsland(i,j,grid)
                    ans+=1
        
        return ans
    
    def removeIsland(self,i, j, grid):
        
        q=deque()
        m=len(grid)
        n=len(grid[0])
        q.append([i,j])
        steps=[[0,1],[1,0],[-1,0],[0,-1]]
        
        while q:
            
            i,j=q.popleft()
            for step in steps:
                
                x=i+step[0]
                y=j+step[1]
                
                if 0<=x<m and 0<=y<n and grid[x][y]=='1':
                    grid[x][y]='0'
                    q.append((x,y))