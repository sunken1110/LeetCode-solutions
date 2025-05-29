#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/description

# Time Complexity O((m+n)*k), Space Complexity O(m+n)
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def dfs(node, parent, depth, graph, cnt=1):
            if depth < k:
                for next_node in graph[node]:
                    if next_node == parent:
                        continue

                    cnt += dfs(next_node, node, depth+1, graph)

            return cnt


        m = len(edges1) + 1
        n = len(edges2) + 1

        if k == 0:
            return [1] * m

        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        max2 = 0
        for node in range(n):
            max2 = max(max2, dfs(node, -1, 1, graph2))

        return [dfs(node, -1, 0, graph1) + max2 for node in range(m)]
