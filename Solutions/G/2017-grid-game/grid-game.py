#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/grid-game/description

# Time Complexity O(n)
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_sum = sum(grid[0][1:])
        bottom_sum = 0
        ans = top_sum

        for i in range(1, len(grid[0])):
            top_sum -= grid[0][i]
            bottom_sum += grid[1][i-1]
            temp = max(top_sum, bottom_sum)

            if temp < ans:
                ans = temp

        return ans
