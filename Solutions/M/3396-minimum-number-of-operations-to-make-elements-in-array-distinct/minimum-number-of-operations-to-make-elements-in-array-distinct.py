#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description

# Time Complexity O(n), Space Complexityt O(n)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        check = set()

        for i in range(n-1, -1, -1):
            if nums[i] in check:
                return i//3 + 1

            check.add(nums[i])

        return 0
