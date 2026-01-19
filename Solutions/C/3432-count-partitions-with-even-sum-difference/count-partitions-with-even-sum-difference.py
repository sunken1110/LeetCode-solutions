#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-partitions-with-even-sum-difference/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0
