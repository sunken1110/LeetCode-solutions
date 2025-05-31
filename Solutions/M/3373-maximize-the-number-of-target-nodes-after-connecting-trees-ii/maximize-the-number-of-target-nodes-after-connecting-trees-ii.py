#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/description

# Time Complexity O(m+n), Space Complexity O(m+n)
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def dfs(graph, n):
            queue = deque([(0, -1, True)])
            parity = [-1] * n

            while queue:
                node, parent, even = queue.popleft()
                parity[node] = even

                for child in graph[node]:
                    if child == parent:
                        continue
                    
                    queue.append((child, node, not even))

            return parity


        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        m = len(edges1) + 1
        n = len(edges2) + 1
        even1 = dfs(graph1, m)
        even2 = dfs(graph2, n)
        sum1 = sum(even1)
        sum2 = sum(even2)

        max2 = max(sum2, n-sum2)

        return [max2 + (sum1 if even else m-sum1) for even in even1]