# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        mapp={}
        q=deque()
        ans=[]
        if root: q.append((root,0,0))

        while q:

            node=q.popleft()
            if node[1] in mapp:
                if node[2] in mapp[node[1]]:
                    mapp[node[1]][node[2]].append(node[0].val)
                else:
                    mapp[node[1]][node[2]] = [node[0].val]
            else:
                mapp[node[1]] = {node[2]: [node[0].val]}
            if node[0].left: q.append((node[0].left, node[1]-1, node[2]+1))
            if node[0].right: q.append((node[0].right, node[1]+1, node[2]+1))

        for i in sorted(mapp):
            temp=[]
            for j in sorted(mapp[i]):
                temp+=sorted(mapp[i][j])
            ans.append(temp)
        return ans