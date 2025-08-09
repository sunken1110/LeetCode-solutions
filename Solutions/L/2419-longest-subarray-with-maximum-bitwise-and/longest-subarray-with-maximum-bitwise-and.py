#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = max(nums)
        max_len = 0
        curr_len = 0
        
        for x in nums:
            if x == n:
                curr_len += 1
                max_len = max(max_len, curr_len)

            else:
                curr_len = 0

        return max_len
