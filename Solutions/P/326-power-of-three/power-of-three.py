#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/power-of-three/description

# Time Complexity O(log(n)), Space Complexity O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n > 1:
            if n % 3 != 0:
                return False

            n //= 3

        return True
