class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:

        adj=[[] for _ in range(n)]
        indegree=[0]*n
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1

        queue=deque()
        count=0
        for i in range(n):
            if not indegree[i]:
                queue.append(i)
                
        while queue:
            node=queue.popleft()
            count+=1
            for i in adj[node]:
                indegree[i]-=1
                if not indegree[i]:
                    queue.append(i)
                        
        if count==n:
            return True
        return False