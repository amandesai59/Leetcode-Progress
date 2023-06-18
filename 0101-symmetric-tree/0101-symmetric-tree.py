# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        left=deque()
        right=deque()

        if root.left:
            left.append(root.left)
        if root.right:
            right.append(root.right)

        while left and right:

            node1=left.popleft()
            node2=right.popleft()

            if (node2 and not node1) or (node1 and not node2) or (node1 and node2 and (node1.val != node2.val)):
                return False
            
            if node1 and node2:
                left.append(node1.left)
                left.append(node1.right)
                right.append(node2.right)
                right.append(node2.left)

        if left or right:
            return False
        return True