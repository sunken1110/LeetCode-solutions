#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/new-21-game/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        windowSum = 1.0
        ans = 0.0

        for i in range(1, n + 1):
            dp[i] = windowSum / maxPts

            if i < k:
                windowSum += dp[i]
            else:
                ans += dp[i]

            if i - maxPts >= 0:
                windowSum -= dp[i - maxPts]

        return ans
