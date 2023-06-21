# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        path=None
        stack=[]
        node=root

        while node or stack:

            if node:
                if node.val==p.val or node.val==q.val:
                    if not path:
                        path=set()
                        for n in stack:
                            path.add(n.val)
                        path.add(node.val)
                    else:
                        temp=stack.pop()
                        while temp.val not in path:
                            temp=stack.pop()
                        return temp
                stack.append(node)
                node=node.left
            else:
                temp=stack[-1]
                if temp.right:
                    node=temp.right
                else:
                    stack.pop()
                    while stack and temp==stack[-1].right:
                        temp=stack.pop()