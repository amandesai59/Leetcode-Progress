# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        mapp={}
        for i,val in enumerate(inorder):
            mapp[val]=i

        return self.rec(preorder, [0,len(preorder)-1], inorder, [0,len(inorder)-1], mapp)
        
    def rec(self, preorder, pre, inorder, inn, mapp):
        if pre[0]>pre[1] or inn[0]>inn[1]:
            return None

        root = TreeNode(preorder[pre[0]])

        rootIndex = mapp[root.val]
        left=rootIndex-inn[0]

        root.left = self.rec(preorder, [pre[0]+1, pre[0]+left], inorder, [inn[0], rootIndex-1], mapp)
        root.right = self.rec(preorder, [pre[0]+left+1,pre[1]], inorder, [rootIndex+1, inn[1]], mapp)

        return root