#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-servers-that-communicate/description

# Complexity O(m*n)
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0

        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1)):
                    cnt += 1
        
        return cnt
