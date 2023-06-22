# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode], isReverse: bool):
        self.stack=[]
        while root:
            self.stack.append(root)
            if isReverse: root=root.right
            else: root=root.left
        self.reverse=isReverse

    def next(self) -> int:
        node=self.stack.pop()

        if not self.reverse:
            temp=node.right
            while temp:
                self.stack.append(temp)
                temp=temp.left
        else:
            temp=node.left
            while temp:
                self.stack.append(temp)
                temp=temp.right

        return node.val

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        left=BSTIterator(root, False)
        right=BSTIterator(root, True)

        i=left.next()
        j=right.next()

        while i<j:
            if i+j == k:
                return True
            elif i+j < k:
                i = left.next()
            else:
                j = right.next()
        return False