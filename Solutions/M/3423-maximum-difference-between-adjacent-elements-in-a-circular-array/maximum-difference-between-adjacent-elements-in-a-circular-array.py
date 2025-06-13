#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description

# Time Complexity O(n), Space Complexityt O(1)
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        prev = nums[0]
        diff = 0

        for num in nums[1:]:
            diff = max(diff, abs(num-prev))
            prev = num

        return max(diff, abs(nums[0]-prev))
