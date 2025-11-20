#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/keep-multiplying-found-values-by-two/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)

        while original in nums:
            original *= 2

        return original
