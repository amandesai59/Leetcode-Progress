# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        curr=root
        ans=[]

        while curr:
            if not curr.left:
                ans.append(curr.val)
                curr=curr.right
            else:
                prev=curr.left
                while prev.right and prev.right!=curr:
                    prev=prev.right
                
                if not prev.right:
                    prev.right=curr
                    curr=curr.left
                else:
                    prev.right=None
                    ans.append(curr.val)
                    curr=curr.right

        self.pointer=-1
        self.n=len(ans)
        self.nodes=ans

    def next(self) -> int:
        self.pointer+=1
        return self.nodes[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer+1 < self.n
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()