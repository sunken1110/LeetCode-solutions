#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/domino-and-tromino-tiling/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1

        elif n == 2:
            return 2

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        prev = dp[0]
        mod = 10**9 + 7

        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2] + 2 * prev) % mod
            prev += dp[i-2]

        return dp[n] % mod
