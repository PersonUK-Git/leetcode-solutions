from collections import defaultdict, deque
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        # Bob simulation - DFS
        bob_times = {} # node on root path -> time visited
        def dfs(src, prev, time):
            if src == 0:
                bob_times[src] = time
                return True

            for nei in adj[src]:
                if nei == prev:
                    continue
                if dfs(nei, src, time + 1):
                    bob_times[src] = time
                    return True
            return False
        dfs(bob, -1, 0)

        # Alice Simulation - BFS
        q = deque([(0, 0, -1, amount[0])]) # (node, time, parent, total profit)
        res = float("-inf")
        while q:
            node, time, parent, profit = q.popleft()
            
            for nei in adj[node]:
                if nei == parent:
                    continue
                nei_profit = amount[nei]
                nei_time = time + 1
                if nei in bob_times:
                    if nei_time > bob_times[nei]:
                        nei_profit = 0
                    if nei_time == bob_times[nei]:
                        nei_profit = nei_profit // 2
                
                q.append((nei, nei_time, node, profit + nei_profit))
                if len(adj[nei]) == 1:
                    res = max(res, profit + nei_profit)
        return res


'''
CPP CODE

#include <vector>
#include <queue>
#include <climits>
using namespace std;

class Solution {
public:
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        int n = amount.size();
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        
        vector<int> bobTime(n, -1);
        dfs(bob, -1, 0, adj, bobTime);
        
        struct State { int node, time, parent, profit; };
        queue<State> q;
        q.push({0, 0, -1, amount[0]});
        int maxProfit = INT_MIN;
        
        while (!q.empty()) {
            auto [cur, t, p, profit] = q.front();
            q.pop();
            
            for (int nei : adj[cur]) {
                if (nei == p) continue;
                
                int neiT = t + 1;
                int neiProfit = amount[nei];
                
                if (bobTime[nei] != -1) {
                    if (neiT < bobTime[nei]) neiProfit = amount[nei];
                    else if (neiT == bobTime[nei]) neiProfit /= 2;
                    else neiProfit = 0;
                }
                
                int total = profit + neiProfit;
                q.push({nei, neiT, cur, total});
                
                // Check if leaf (excluding root)
                if (adj[nei].size() == 1 && nei != 0) {
                    maxProfit = max(maxProfit, total);
                }
            }
        }
        return maxProfit;
    }

private:
    bool dfs(int node, int parent, int time, vector<vector<int>>& adj, vector<int>& bobTime) {
        if (node == 0) {
            bobTime[node] = time;
            return true;
        }
        for (int nei : adj[node]) {
            if (nei == parent) continue;
            if (dfs(nei, node, time + 1, adj, bobTime)) {
                bobTime[node] = time;
                return true;
            }
        }
        return false;
    }
};
'''