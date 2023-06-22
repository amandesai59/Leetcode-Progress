# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.prev=None
        self.first=None
        self.last=None
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val


    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)

        if self.prev and root.val<self.prev.val:
            if not self.first:
                self.first=self.prev
                self.last=root
            else:
                self.last=root

        self.prev=root
        self.inorder(root.right)