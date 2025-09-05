#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/description

# Time Complexity O(60), Space Complexity O(1)
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 1

        while num1 > 0:
            num1 -= num2

            if num1 < k:
                return -1

            if num1.bit_count() <= k:
                return k

            k += 1

        return -1
