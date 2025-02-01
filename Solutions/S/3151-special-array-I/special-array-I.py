#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/special-array-i/description

# Complexity O(n)
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i+1] % 2:
                return False

        return True
