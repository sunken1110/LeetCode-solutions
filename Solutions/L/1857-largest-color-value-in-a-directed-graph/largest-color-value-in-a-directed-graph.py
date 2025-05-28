#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description

# Time Complexity O(n + 26*e), Space Complexity O(26*n) where n is the number of nodes, e is the number of edges
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        visited = 0
        color_cnt = [[0] * 26 for _ in range(n)]
        color_value = 0
        indegree = [0] * n
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque(node for node in range(n) if indegree[node] == 0)

        while queue:
            node = queue.popleft()
            visited += 1
            color = ord(colors[node]) - ord('a')
            color_cnt[node][color] += 1
            color_value = max(color_value, color_cnt[node][color])

            for next_node in graph[node]:
                for c in range(26):
                    color_cnt[next_node][c] = max(color_cnt[next_node][c], color_cnt[node][c])

                indegree[next_node] -= 1

                if indegree[next_node] == 0:
                    queue.append(next_node)

        return color_value if visited == n else -1
