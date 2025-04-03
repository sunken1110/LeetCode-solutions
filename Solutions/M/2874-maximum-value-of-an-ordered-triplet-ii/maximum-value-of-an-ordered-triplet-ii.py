#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/description

# Complexity O(n)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        max_ij = 0
        max_i = 0

        for num in nums:
            ans = max(ans, max_ij * num)
            max_ij = max(max_ij, max_i-num)
            max_i = max(max_i, num)

        return ans
