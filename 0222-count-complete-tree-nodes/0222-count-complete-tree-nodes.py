# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        q=deque([[root, 1]])

        while q:

            n=len(q)
            for _ in range(n):
                node, x=q.popleft()
                if node.left:
                    q.append([node.left, 2*x])
                else:
                    return 2*x-1
                if node.right:
                    q.append([node.right, 2*x+1])
                else:
                    return 2*x

        return x