#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-difference-between-increasing-elements/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        prev_min = nums[0]

        for num in nums[1:]:
            if num == prev_min:
                continue

            elif num < prev_min:
                prev_min = num

            else:
                max_diff = max(max_diff, num-prev_min)

        return max_diff