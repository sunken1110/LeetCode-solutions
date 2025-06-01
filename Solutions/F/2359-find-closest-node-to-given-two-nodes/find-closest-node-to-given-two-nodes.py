#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [-1] * n
        dist2 = [-1] * n
        queue = deque([(node1, 0, 1), (node2, 0, 2)])
        ans = []
        
        while queue:
            node, depth, i = queue.popleft()

            if i == 1:
                if dist1[node] >= 0:
                    continue

                dist1[node] = depth

            else:
                if dist2[node] >= 0:
                    continue

                dist2[node] = depth

            if dist1[node] != -1 and dist2[node] != -1:
                heapq.heappush(ans, (max(dist1[node], dist2[node]), node))

            elif edges[node] != -1:
                queue.append([edges[node], depth+1, i])

        return ans[0][1] if ans else -1
