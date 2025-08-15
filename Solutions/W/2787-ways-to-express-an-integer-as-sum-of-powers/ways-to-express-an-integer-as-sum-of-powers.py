#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description

# Time Complexity O(n^(1+1/x)), Space Complexity O(n)
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        powers = []
        i = 1
        mod = 10**9 + 7

        while True:
            p = pow(i, x)

            if p > n:
                break

            powers.append(p)
            i += 1

        dp = [0] * (n+1)
        dp[0] = 1

        for p in powers:
            for p_sum in range(n, p-1, -1):
                dp[p_sum] = (dp[p_sum] + dp[p_sum-p]) % mod

        return dp[n] % mod
