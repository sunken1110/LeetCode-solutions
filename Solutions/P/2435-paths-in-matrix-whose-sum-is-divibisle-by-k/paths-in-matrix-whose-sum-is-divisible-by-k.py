#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/description

# Time Complexity O(m*n*k), Space Complexity O(m*n*k)
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[0] * k for j in range(n)] for i in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        mod = 10**9 + 7

        for i in range(m):
            for j in range(n):
                for prev in range(k):
                    curr = (prev + grid[i][j]) % k

                    if i > 0:
                        dp[i][j][curr] += dp[i-1][j][prev]

                    if j > 0:
                        dp[i][j][curr] += dp[i][j-1][prev]

                    dp[i][j][curr] %= mod

        return dp[m-1][n-1][0]
