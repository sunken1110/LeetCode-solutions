#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description

# Complexity O(m*n)
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        costs = {}
        not_visited = deque([[0, 0, 0]])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 1: right, 2: left, 3: up, 4: down

        while not_visited:
            x, y, cost = not_visited.popleft()

            while 0 <= x < m and 0 <= y < n and (x, y) not in costs:
                costs[x, y] = cost
                
                for d in directions:
                    not_visited.append([x + d[0], y + d[1], cost + 1]) # if 

                dx, dy = directions[grid[x][y] - 1] # index adjust

                x += dx
                y += dy

        return costs[m-1, n-1]
