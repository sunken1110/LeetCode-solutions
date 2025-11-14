#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        prev_ones = 0
        prev_zeroes = 0


        for num in s:
            if num == '0':
                prev_zeroes = 1

            else:
                ans += prev_ones * prev_zeroes
                prev_ones += 1
                prev_zeroes = 0

        ans += prev_ones * prev_zeroes

        return ans
