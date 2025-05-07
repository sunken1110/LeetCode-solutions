#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/build-array-from-permutation/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n):
            ans.append(nums[nums[i]])

        return ans
