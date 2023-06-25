# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap=[]
        for root in lists:
            while root:
                heappush(heap, root.val)
                root=root.next

        root=ListNode(-1)
        node=root
        for i in range(len(heap)):
            node.next = ListNode(heappop(heap))
            node=node.next
        
        return root.next