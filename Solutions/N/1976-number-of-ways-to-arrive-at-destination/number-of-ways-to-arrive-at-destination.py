#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description

# Complexity O(m*log(n))
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        times = [inf] * n
        mod = 10**9 + 7
        cnt = [0] * n

        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        times[0] = 0
        cnt[0] = 1
        queue = [(0, 0)] # time, node for min_heap

        while queue:
            time, node = heappop(queue)

            if times[node] < time:
                continue

            for next_node, t in graph[node]:
                if times[node] + t < times[next_node]:
                    times[next_node] = times[node] + t
                    cnt[next_node] = cnt[node]

                    heappush(queue, (times[next_node], next_node))

                elif times[node] + t == times[next_node]:
                    cnt[next_node] = (cnt[next_node] + cnt[node]) % mod

        return cnt[n-1]
