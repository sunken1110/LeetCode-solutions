#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-ascending-subarray-sum/description

# Complexity O(n)
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                curr_sum += nums[i]

            elif nums[i-1] >= nums[i]:
                max_sum = max(max_sum, curr_sum)
                curr_sum = nums[i]

        return max(max_sum, curr_sum)
