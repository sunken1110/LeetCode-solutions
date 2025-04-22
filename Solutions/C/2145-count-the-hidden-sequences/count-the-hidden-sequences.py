#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-the-hidden-sequences/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix_min = 0
        prefix_max = 0
        prefix = 0

        for diff in differences:
            prefix += diff

            if prefix_min > prefix:
                prefix_min = prefix

            if prefix_max < prefix:
                prefix_max = prefix

        return max(0, (upper-lower) - (prefix_max-prefix_min) + 1)
