#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        curr_min = -1
        curr_max = -1
        left = 0
        cnt = 0

        for right, num in enumerate(nums):
            if num == minK:
                curr_min = right

            if num == maxK:
                curr_max = right

            if num < minK or num > maxK:
                left = right + 1
                curr_min = -1
                curr_max = -1

            if curr_min != -1 and curr_max != -1:
                cnt += min(curr_min, curr_max) - left + 1

        return cnt
