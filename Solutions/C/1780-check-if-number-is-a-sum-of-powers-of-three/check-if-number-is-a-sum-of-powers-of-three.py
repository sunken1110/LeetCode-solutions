#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description

# Complexity O(n)
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            digit = n % 3
            if digit == 2:
                return False

            n = n // 3

        return True
