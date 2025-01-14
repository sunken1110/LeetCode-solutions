#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-length-of-string-after-operations/description

# Complexity O(n)
class Solution:
    def minimumLength(self, s: str) -> int:
        ans = 0
        
        for char in set('abcdefghijklmnopqrstuvwxyz'):
            cnt = s.count(char)

            if cnt != 0:
                ans += 2 - (cnt % 2) # 1 if odd, 2 if even

        return ans
