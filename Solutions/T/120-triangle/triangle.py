#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/triangle/description

# Time Complexity O(n^2), Space Complexity O(n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1]

        for i in range(n-2, -1, -1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])

        return dp[0]
