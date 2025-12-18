#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-covered-buildings/description

# Time Complexity O(n^2), Space Complexity O(n)
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        max_x = [0] * (n+1)
        min_x = [n+1] * (n+1)
        max_y = [0] * (n+1)
        min_y = [n+1] * (n+1)
        cnt = 0

        for x, y in buildings:
            max_x[y] = max(max_x[y], x)
            min_x[y] = min(min_x[y], x)
            max_y[x] = max(max_y[x], y)
            min_y[x] = min(min_y[x], y)

        for x, y in buildings:
            if min_x[y] < x < max_x[y] and min_y[x] < y < max_y[x]:
                cnt += 1

        return cnt
