# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root: q=deque([root])
        else: return ''
        ans=''

        while q:
            node=q.popleft()
            if node:
                ans+=str(node.val)+','
                q.append(node.left)
                q.append(node.right)
            else:
                ans+='null,'

        return ans[:-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes=data.split(',')
        n=len(nodes)
        i=1
        root=TreeNode(nodes[0])
        q=deque([root])

        while i<n:
            parent=q.popleft()
            if nodes[i]!='null':
                parent.left=TreeNode(nodes[i])
                q.append(parent.left)
            if nodes[i+1]!='null':
                parent.right=TreeNode(nodes[i+1])
                q.append(parent.right)
            i+=2

        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))