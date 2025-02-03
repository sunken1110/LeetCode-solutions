#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description

# Complexity O(n)
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0
        
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                cnt += 1
            if cnt > 1:
                return False

        return True
