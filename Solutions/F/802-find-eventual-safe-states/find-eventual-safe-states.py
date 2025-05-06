#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-eventual-safe-states/description

# Time Complexity O(v+e) where v is the number of nodes and e is the number of edges
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [-1] * n
        visited = set()
        ans = []


        def dfs(node):
            if safe[node] == 1 or len(graph[node]) == 0:
                return True

            if safe[node] == 0 or node in visited:
                return False

            visited.add(node)

            for next_node in graph[node]:
                if not dfs(next_node):
                    safe[next_node] = 0
                    return False

            safe[node] = 1

            return True

        
        for i in range(n):
            if dfs(i):
                ans.append(i)

        return ans
