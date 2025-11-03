#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description

# Time Complexity O(m*n), Space Complexity O(m*n)
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        occupied = [[0] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i, j in guards:
            occupied[i][j] = 1

        for i, j in walls:
            occupied[i][j] = 2

        for x, y in guards:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                while m > nx > -1 and n > ny > -1 and occupied[nx][ny] not in [1, 2]:
                    occupied[nx][ny] = 3
                    nx += dx
                    ny += dy

        return sum(occupied[i][j] == 0 for i in range(m) for j in range(n))
