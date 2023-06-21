# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        node=root
        parent=None
        isLeft=1

        while node:
            if node.val>key:
                parent=node
                isLeft=1
                node=node.left
            elif node.val<key:
                parent=node
                isLeft=0
                node=node.right
            else:
                break

        if node:
            if node.left:
                temp=node.left
                while temp.right:
                    temp=temp.right
                temp.right=node.right
                node=node.left
            else:
                node=node.right

            if parent:
                if isLeft:
                    parent.left=node
                else:
                    parent.right=node
            else:
                return node
        return root
        