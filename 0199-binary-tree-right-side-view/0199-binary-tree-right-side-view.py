# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q=deque()
        mapp={}
        if root: q.append([root, [0,0]])

        while q:

            node = q.popleft()

            x,y=node[1]

            # if (y in mapp and (x > mapp[y][1])) or (y not in mapp):
            mapp[y] = [node[0].val, x]
            if node[0].left: q.append([node[0].left, [x-1, y+1]])
            if node[0].right: q.append([node[0].right, [x+1, y+1]])
            
        ans=[]
        for i in sorted(mapp):
            ans.append(mapp[i][0])
        return ans