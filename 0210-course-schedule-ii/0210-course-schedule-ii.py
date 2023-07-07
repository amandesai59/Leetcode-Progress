class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:

        adj=[[] for _ in range(n)]
        indegree=[0]*n
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1

        queue=deque()
        ans=[]
        for i in range(n):
            if not indegree[i]:
                queue.append(i)
                
        while queue:
            node=queue.popleft()
            ans.append(node)
            for i in adj[node]:
                indegree[i]-=1
                if not indegree[i]:
                    queue.append(i)
                        
        if len(ans)==n:
            return ans
        return []