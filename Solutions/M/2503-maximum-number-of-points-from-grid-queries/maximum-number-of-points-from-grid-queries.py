#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description

# Time Complexity O(mn + q*log(q))
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        queries = sorted([(val, idx) for idx, val in enumerate(queries)])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        ans = [0] * len(queries)
        pts = 0

        for val, idx in queries:
            while queue and queue[0][0] < val:
                pts += 1
                v, x, y = heappop(queue)

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        heappush(queue, (grid[nx][ny], nx, ny))
                        visited[nx][ny] = True

            ans[idx] = pts

        return ans

