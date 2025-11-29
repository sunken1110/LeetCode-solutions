#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description

# Time Complexity O(n), Space Complexityt O(1)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
