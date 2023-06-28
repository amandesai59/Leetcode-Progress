class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq={}
        for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1

        heap=[[-freq[i], i] for i in freq]
        heapq.heapify(heap)

        ans=[]
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans