#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/longest-nice-subarray/description

# Complexity O(n)
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        max_cnt = 1
        curr = 0

        for right, num in enumerate(nums):
            while left < right and curr & num != 0:
                curr ^= nums[left]
                left += 1

            curr |= num
            max_cnt = max(max_cnt, right - left + 1)

        return max_cnt
