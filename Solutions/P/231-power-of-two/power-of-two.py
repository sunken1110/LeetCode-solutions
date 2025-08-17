#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/power-of-two/description

# Time Complexity O(log(n)), Space Complexity O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 2 != 0:
                return False

            n //= 2

        return True
