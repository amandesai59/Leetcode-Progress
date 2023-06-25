class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap=MaxHeap(nums)
        ans = None
        while k:
            ans = heap.extraxtMax()
            k-=1
            
        return ans
            
            
class MaxHeap:
    
    def __init__(self, nums=None):
        self.heap=[]
        
        for n in nums:
            self.insert(n)
    
    def insert(self, x):
        heappush(self.heap, -x)
        
    def extraxtMax(self):
        return -heappop(self.heap)