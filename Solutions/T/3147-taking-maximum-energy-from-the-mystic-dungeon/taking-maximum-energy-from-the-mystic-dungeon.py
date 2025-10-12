#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        suffix_sum = energy[::-1]

        for i in range(k, n):
            suffix_sum[i] += suffix_sum[i-k]

        return max(suffix_sum)
