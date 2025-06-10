#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description

# Time Complexity O(n), Space Complexityt O(n)
class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        max_odd = 0
        min_even = inf

        for char, cnt in freq.items():
            if cnt % 2 == 0:
                min_even = min(min_even, cnt)

            else:
                max_odd = max(max_odd, cnt)

        return max_odd - min_even
