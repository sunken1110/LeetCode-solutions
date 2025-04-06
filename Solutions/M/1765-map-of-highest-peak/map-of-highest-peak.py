#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/map-of-highest-peak/description

# Time Complexity O(n)
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])

        heights = [[-1] * n for _ in range(m)]
        visited = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    heights[i][j] = 0
                    visited.append((i, j, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while visited:
            x, y, h = visited.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] == -1:
                    heights[nx][ny] = h+1
                    visited.append((nx, ny, h+1))

        return heights

