#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/smallest-number-with-all-set-bits/description

# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def smallestNumber(self, n: int) -> int:
        return 2**int(log2(n) + 1) - 1
