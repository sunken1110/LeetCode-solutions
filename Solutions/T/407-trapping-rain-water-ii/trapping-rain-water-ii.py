#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/trapping-rain-water-ii/description

# Complexity O(mn*log(mn)))
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False] * n for _ in range(m)]
        queue = []
        vol = 0

        for i in range(m):
            for j in [0, n-1]:
                heappush(queue, (heightMap[i][j], i, j))
                visited[i][j] = True

        for j in range(1, n-1):
            for i in [0, m-1]:
                heappush(queue, (heightMap[i][j], i, j))
                visited[i][j] = True

        while queue:
            h, x, y = heappop(queue)

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    vol += max(0, h - heightMap[nx][ny])
                    visited[nx][ny] = True

                    heappush(queue, (max(h, heightMap[nx][ny]), nx, ny))

        return vol
