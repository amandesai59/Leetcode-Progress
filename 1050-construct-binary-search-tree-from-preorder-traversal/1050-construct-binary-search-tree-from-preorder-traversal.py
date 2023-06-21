# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        return self.rec(preorder, 0, len(preorder)-1)

    def rec(self, preorder,start, end):

        if start>end:
            return None

        i=start+1
        root=TreeNode(preorder[start])
        
        while i<=end and preorder[i]<root.val:
            i+=1
        root.left=self.rec(preorder, start+1, i-1)
        root.right=self.rec(preorder, i, end)

        return root