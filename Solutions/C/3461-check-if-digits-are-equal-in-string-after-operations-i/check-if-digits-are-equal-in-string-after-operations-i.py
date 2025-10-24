#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description

# Time Complexity O(n^2), Space Complexity O(n)
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(s)
        n = len(s)

        while n > 2:
            for i in range(n-1):
                s[i] = str((int(s[i]) + int(s[i+1])) % 10)
                
            n -= 1

        return s[0] == s[1]
