#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description

# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num_m = n // m

        return n*(n+1)//2 - m*num_m*(num_m+1)
