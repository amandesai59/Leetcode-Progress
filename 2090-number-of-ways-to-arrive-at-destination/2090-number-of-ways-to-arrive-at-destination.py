class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        adj=[[] for _ in range(n)]
        for road in roads:
            adj[road[0]].append([road[1],road[2]])
            adj[road[1]].append([road[0],road[2]])

        heap=[]
        heapq.heappush(heap, [0,0])
        minTime=[float('inf')]*n
        minTime[0]=0
        ways=[0]*n
        ways[0]=1
        mod = int(1e9 + 7)

        while heap:
            time, node=heapq.heappop(heap)

            for i, weight in adj[node]:
                if minTime[i]>time+weight:
                    minTime[i]=time+weight
                    ways[i]=ways[node]
                    heapq.heappush(heap, [minTime[i], i])
                elif (time+weight)==minTime[i]:
                    ways[i]+=ways[node]%mod

        return ways[-1]%mod