#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-lucky-integer-in-an-array/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        lucky = -1

        for num, val in freq.items():
            if num == val:
                lucky = max(lucky, num)

        return lucky
