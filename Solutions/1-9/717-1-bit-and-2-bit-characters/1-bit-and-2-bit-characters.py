#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/1-bit-and-2-bit-characters/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        prev = -1

        for bit in bits:
            if prev == 1:
                prev = -1
                continue

            prev = bit

        return prev == 0
