# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        return self.maxSum(root)[1]

    def maxSum(self, root: Optional[TreeNode]):

        if root==None:
            return [0,-1001]

        left=self.maxSum(root.left)
        right=self.maxSum(root.right)

        curr=root.val + max(left[0], right[0])
        return [max(curr,0), max([left[1], right[1], root.val+left[0]+right[0]])]