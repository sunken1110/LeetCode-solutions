#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/water-bottles/description

# Time Complexity O(log(n)), Space Complexity O(1)
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt = numBottles

        while numBottles >= numExchange:
            q, r = divmod(numBottles, numExchange)
            cnt += q
            numBottles = q + r

        return cnt
