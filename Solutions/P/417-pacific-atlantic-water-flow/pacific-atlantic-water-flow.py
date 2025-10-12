#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/pacific-atlantic-water-flow/description

# Time Complexity O(m*n), Space Complexity O(m*n)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        def dfs(x, y, visited):
            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and heights[x][y] <= heights[nx][ny]:
                    dfs(nx, ny, visited)


        for x in range(m):
            dfs(x, 0, pacific)
            dfs(x, n-1, atlantic)

        for y in range(n):
            dfs(0, y, pacific)
            dfs(m-1, y, atlantic)


        return list(pacific & atlantic)
