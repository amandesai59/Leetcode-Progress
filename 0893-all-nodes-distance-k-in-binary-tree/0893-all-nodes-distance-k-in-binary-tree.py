# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        parent={}
        q=deque([root])

        while q:

            node=q.popleft()
            if node.left:
                q.append(node.left)
                parent[node.left]=node
            if node.right:
                q.append(node.right)
                parent[node.right]=node

        q=deque([target])
        visited={target}
        ans=[]

        while q:

            if not k:
                break

            n=len(q)
            for _ in range(n):
                node=q.popleft()

                if node.left and (node.left not in visited):
                    q.append(node.left)
                    visited.add(node.left)
                if node.right and (node.right not in visited):
                    q.append(node.right)
                    visited.add(node.right)
                if (node in parent) and (parent[node] not in visited):
                    q.append(parent[node])
                    visited.add(parent[node])
            k-=1

        return [temp.val for temp in q]