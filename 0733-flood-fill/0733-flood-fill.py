class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        queue=deque([[sr,sc]])
        prev=image[sr][sc]
        n=len(image)
        m=len(image[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        visited=[row[:] for row in image]

        while queue:
            x,y=queue.popleft()
            image[x][y]=color
            visited[x][y]=-1
            for d in directions:
                if self.valid(x+d[0],y+d[1],n,m) and image[x+d[0]][y+d[1]]==prev and visited[x+d[0]][y+d[1]]!=-1:
                    queue.append([x+d[0], y+d[1]])
        return image

    def valid(self, x, y, n, m):
        if x>=0 and x<n and y>=0 and y<m:
            return True
        return False