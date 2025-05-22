#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def numOfWays(self, n: int) -> int:
        aba = 6
        abc = 6
        mod = 10**9 + 7

        for _ in range(n-1):
            aba, abc = (3*aba + 2*abc) % mod, (2*aba + 2*abc) % mod

        return (aba+abc) % mod
