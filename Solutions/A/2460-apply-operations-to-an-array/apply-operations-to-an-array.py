#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/apply-operations-to-an-array/description

# Complexity O(n)
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        non_zero = 0
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero] = nums[i]
                non_zero += 1

        while non_zero < n:
            nums[non_zero] = 0
            non_zero += 1

        return nums
