#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/description

# Time Complexity O(log(k)), Space Complexity O(1)
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        shifts = 0

        while k != 1:
            digit = k.bit_length() - 1

            if (1 << digit) == k:
                digit -= 1

            k -= (1 << digit)

            if operations[digit]:
                shifts += 1

        return chr((shifts % 26) + ord('a'))
