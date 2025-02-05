#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/making-a-large-island/description

# Complexity O(m*n)
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        potential_area = defaultdict(int) 

        def dfs(node):
            q = deque([node])
            area = 1
            near_land = set()
            
            while q:
                x, y = q.popleft()

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            q.append((nx, ny))
                            grid[nx][ny] = -1
                            area += 1

                        elif grid[nx][ny] == 0:
                            near_land.add((nx, ny))

            for water in near_land:
                potential_area[water] += area

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    grid[x][y] = -1
                    dfs((x, y))

        if potential_area:
            return 1 + max(potential_area.values())

        elif grid[0][0] == 0:
            return 1

        else:
            return m * n
