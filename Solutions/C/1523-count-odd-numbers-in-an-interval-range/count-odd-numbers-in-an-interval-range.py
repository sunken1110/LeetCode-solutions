#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description

# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1) // 2 - low // 2
