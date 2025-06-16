#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        max_num = num
        min_num = num

        for digit in num:
            if digit != '9':
                max_num = num.replace(digit, '9')
                break

        for idx, digit in enumerate(num):
            if digit not in ['0', '1']:
                if idx == 0:
                    min_num = num.replace(digit, '1')
                    
                else:
                    min_num = num.replace(digit, '0')

                break

        return int(max_num) - int(min_num)
