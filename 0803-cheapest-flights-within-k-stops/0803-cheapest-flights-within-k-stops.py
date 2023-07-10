class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj=[[] for _ in range(n)]
        for flight in flights:
            adj[flight[0]].append([flight[1],flight[2]])

        queue=deque([[0, 0, src]])
        prices=[1e9]*n
        
        while queue:
            price, currK, node=queue.popleft()

            if currK>k:
                continue

            for i, weight in adj[node]:
                if prices[i]>price+weight:
                    prices[i]=price+weight
                    queue.append([prices[i], currK+1, i])

        return prices[dst] if prices[dst]!=1e9 else -1