#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/power-of-four/description

# Time Complexity O(log(n)), Space Complexity O(1)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False

        while n > 1:
            if n % 4 != 0:
                return False

            n //= 4

        return True
