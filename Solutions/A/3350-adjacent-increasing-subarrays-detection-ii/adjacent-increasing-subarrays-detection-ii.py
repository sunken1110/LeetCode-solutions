#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        curr = 1
        prev = 0
        k = 0

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                curr += 1

            else:
                k = max(k, curr // 2, min(curr, prev))
                prev = curr
                curr = 1

        return max(k, curr // 2, min(curr, prev))
