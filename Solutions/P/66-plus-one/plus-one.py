#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/plus-one/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n-1, -1, -1):
            digits[i] += 1

            if digits[i] < 10:
                return digits

            digits[i] = 0

        return [1] + [0] * n
