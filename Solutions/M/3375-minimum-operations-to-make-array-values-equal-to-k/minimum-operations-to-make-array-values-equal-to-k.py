#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = set(nums)

        if k > min(nums):
            return -1

        elif k == min(nums):
            return len(nums) - 1

        else:
            return len(nums)
