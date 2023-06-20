# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr=root
        ans=[]

        while curr:
            if not curr.left:
                ans.append(curr)
                curr=curr.right
            else:
                prev=curr.left
                while prev.right and prev.right!=curr:
                    prev=prev.right
                
                if not prev.right:
                    prev.right=curr
                    ans.append(curr)
                    curr=curr.left
                else:
                    prev.right=None
                    curr=curr.right

        prev=root
        for node in ans[1:]:
            prev.right=node
            prev.left=None
            prev=node
