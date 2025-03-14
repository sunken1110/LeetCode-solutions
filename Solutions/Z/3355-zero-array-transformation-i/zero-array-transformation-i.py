#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/zero-array-transformation-i/description

# Complexity O(n)
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        pref = [0] * (n+1)
        psum = 0

        for l, r in queries:
            pref[l] += 1
            pref[r+1] -= 1

        for i in range(n):
            psum += pref[i]

            if nums[i] > psum:
                return False

        return True
