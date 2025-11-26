#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/smallest-integer-divisible-by-k/description

# Time Complexity O(k), Space Complexity O(1)
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        curr = 0

        for digit in range(1, k+1):
            curr = (curr * 10 + 1) % k

            if curr == 0:
                return digit

        return -1
