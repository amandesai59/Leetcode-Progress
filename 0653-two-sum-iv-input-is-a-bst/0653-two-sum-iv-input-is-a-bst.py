# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        stack=[]
        nums=[]

        while root or stack:
            while root:
                stack.append(root)
                root=root.left

            root=stack.pop()
            nums.append(root.val)
            root=root.right

        visited=set()
        for n in nums:
            if (k-n) in visited:
                return True
            visited.add(n)

        return False