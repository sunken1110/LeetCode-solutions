#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/reordered-power-of-2/description

# Time Complexity O(log(n)), Space Complexity O(log(n))
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = sorted(str(n))

        return digits in (sorted(str(1<<x)) for x in range(30))
