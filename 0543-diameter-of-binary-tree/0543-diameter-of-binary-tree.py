# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        return self.maxDepth(root)[1]


    def maxDepth(self, root: Optional[TreeNode]):

        if root==None:
            return [0,0]

        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)

        return [1 + max(left[0],right[0]), max([left[1], right[1], left[0]+right[0]])]