#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(int(floor(log10(num))) % 2 == 1 for num in nums)
