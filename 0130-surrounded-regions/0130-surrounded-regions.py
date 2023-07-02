from queue import Queue
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=len(board)
        m=len(board[0])
        visited=[[0 for _ in range(m)] for _ in range(n)]
        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        for i in range(1, n-1):
            for j in range(1, m-1):
                if board[i][j]=='O' and visited[i][j]==0:
                    visited[i][j]=1
                    self.bfs(board, visited, i, j, n, m, directions)
        

    def bfs(self, board, visited, x, y, n, m, directions):

        queue=Queue()
        queue.put([x,y])
        region=[[x,y]]
        flag=False

        while queue.qsize():
            i,j=queue.get()

            for d in directions:
                p=i+d[0]
                q=j+d[1]

                if p>=0 and q>=0 and p<n and q<m and visited[p][q]==0 and board[p][q]=='O':
                    visited[p][q]=1
                    if p==n-1 or q==m-1 or p==0 or q==0:
                        flag=True
                    queue.put([p,q])
                    region.append([p,q])
        if flag:
            return
        for x,y in region:
            board[x][y]='X'