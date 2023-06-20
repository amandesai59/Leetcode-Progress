# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        mapp={}
        for i,val in enumerate(inorder):
            mapp[val]=i

        return self.rec(postorder, [0,len(postorder)-1], inorder, [0,len(inorder)-1], mapp)

    def rec(self, postorder, post, inorder, inn, mapp):

        if post[0]>post[1] or inn[0]>inn[1]:
            return None

        root = TreeNode(postorder[post[1]])
        rootIndex = mapp[root.val]
        right=inn[1]-rootIndex

        root.right = self.rec(postorder, [post[1]-right, post[1]-1], inorder, [rootIndex+1, inn[1]], mapp)
        root.left = self.rec(postorder, [post[0],post[1]-right-1], inorder, [inn[0], rootIndex-1], mapp)
        return root