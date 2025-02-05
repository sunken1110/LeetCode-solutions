#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description

# Complexity O(n)
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_len = 1

        # strictly increasing case
        curr_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_len += 1
                max_len = max(max_len, curr_len)

            else:
                curr_len = 1

        #strictrly decreasing case
        curr_len = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                curr_len += 1
                max_len = max(max_len, curr_len)

            else:
                curr_len = 1

        return max_len
