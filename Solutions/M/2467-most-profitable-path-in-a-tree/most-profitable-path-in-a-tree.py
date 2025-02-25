#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/most-profitable-path-in-a-tree/description

# Complexity O(n)
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        graph = defaultdict(list)
        bob_arrival = [inf] * n
        parents = [-1] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        #--------------------------------

        def link_nodes(node, parent):
            parents[node] = parent

            for child in graph[node]:
                if child == parent:
                    continue

                link_nodes(child, node)

        link_nodes(0, -1)

        #--------------------------------

        bob_loc = bob
        bob_step = 0

        while bob_loc != -1:
            bob_arrival[bob_loc] = bob_step
            bob_step += 1
            bob_loc = parents[bob_loc]

        #--------------------------------

        def dfs(node, step, parent):
            max_sum = -inf
            find_leaf = True

            if step < bob_arrival[node]:
                alice = amount[node]

            elif step == bob_arrival[node]:
                alice = amount[node]//2

            else:
                alice = 0


            for child in graph[node]:
                if child == parent:
                    continue

                find_leaf = False
                max_sum = max(max_sum, dfs(child, step + 1, node))

            return alice + max_sum if not find_leaf else alice

        return dfs(0, 0, -1)
