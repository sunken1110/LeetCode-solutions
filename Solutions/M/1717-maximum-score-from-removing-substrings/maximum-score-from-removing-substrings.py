#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-score-from-removing-substrings/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        pt = 0
        a = 0
        b = 0
        
        if y > x:
            s = s[::-1]
            y, x = x, y

        for char in s:
            if char == 'a':
                a += 1

            elif char == 'b':
                if a > 0:
                    a -= 1
                    pt += x
                
                else:
                    b += 1

            else:
                pt += y * min(a, b)
                a = 0
                b = 0

        return pt + y * min(a, b)
