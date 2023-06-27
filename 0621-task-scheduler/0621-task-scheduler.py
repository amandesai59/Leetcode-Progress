class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        if not n:
            return len(tasks)

        mapp={}
        for t in tasks:
            if t in mapp:
                mapp[t]+=1
            else:
                mapp[t]=1

        heap = [-i for i in mapp.values()]

        heapq.heapify(heap)

        queue=deque()

        currTime=0

        while heap or queue:

            currTime+=1
            if heap:
                freq = -heapq.heappop(heap)

                freq-=1

                if freq:
                    queue.append([freq, currTime+n])

            while queue and queue[0][1]==currTime:
                heapq.heappush(heap, -queue.popleft()[0])

        return currTime