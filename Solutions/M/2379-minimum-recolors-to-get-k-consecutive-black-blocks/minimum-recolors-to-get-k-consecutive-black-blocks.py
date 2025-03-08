#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description

# Complexity O(n)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        consec = blocks[0:k]
        min_ops = ops = consec.count('W')

        for i in range(n-k):
            left = 0 if blocks[i] == 'B' else 1
            right = 0 if blocks[i+k] == 'B' else 1

            ops += right - left
            min_ops = min(min_ops, ops)

        return min_ops
