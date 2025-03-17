#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/divide-array-into-equal-pairs/description

# Complexity O(n)
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums = Counter(nums)

        for freq in nums.values():
            if freq % 2 != 0:
                return False

        return True
