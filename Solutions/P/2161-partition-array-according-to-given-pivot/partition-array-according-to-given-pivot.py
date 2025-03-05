#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/partition-array-according-to-given-pivot/description

# Complexity O(n)
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        center = []
        right = []

        for num in nums:
            if num < pivot:
                left.append(num)

            elif num > pivot:
                right.append(num)

            else:
                center.append(num)

        return left + center + right
