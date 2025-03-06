#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-total-number-of-colored-cells/description

# Complexity O(1)
class Solution:
    def coloredCells(self, n: int) -> int:
        return 2*n*(n-1) + 1
