#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        max_num = num
        min_num = num

        for digit in num:
            if digit != '9':
                max_num = num.replace(digit, '9')
                break

        for digit in num:
            if digit != '0':
                min_num = num.replace(digit, '0')
                break

        return int(max_num) - int(min_num)
