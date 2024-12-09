from collections import deque
from typing import List




class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i + 1] for i in range(n)]
        def shortestDistance():
            q = deque()
            q.append((0, 0))
            visit = set()
            visit.add((0,0))
            while q:
                cur, length = q.popleft()
                if cur == n - 1:
                    return length
                for nei in adj[cur]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, length + 1))
            
        res = []
        for src, dst in queries:
            adj[src].append(dst)
            res.append(shortestDistance())
        return res

arr = [[1, 2], [3, 4]] 

for i in range(len(arr)):
    print(f"i: {i}")
    print(f"arr[i]: {arr[i]}")
    print(f"res[i]: {res[i]}")
    print()