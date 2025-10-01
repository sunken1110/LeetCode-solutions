#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description

# Time Complexity O(n^3), Space Complexity O(n^2)
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j] if dp[i][j] != 0 else inf,
                             dp[i][k] + dp[k][j] + values[i]*values[j]*values[k])

        return dp[0][n-1]
