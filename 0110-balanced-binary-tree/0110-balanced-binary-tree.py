# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if self.maxDepth(root)==-1:
            return False
        return True

    def maxDepth(self, root: Optional[TreeNode]):

        if root==None:
            return 0

        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)

        if left==-1 or right==-1 or abs(left-right)>1:
            return -1
        return 1 + max(left,right)