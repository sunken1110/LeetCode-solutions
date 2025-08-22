#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        bottom, top, left, right = len(grid), -1,len(grid[0]), -1

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col:
                    bottom = min(bottom, i)
                    top = max(top, i)
                    left = min(left, j)
                    right = max(right, j)

        return (top-bottom+1) * (right-left+1)
