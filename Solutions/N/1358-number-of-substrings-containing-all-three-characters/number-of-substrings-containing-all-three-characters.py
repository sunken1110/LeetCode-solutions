#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description

# Complexity O(n)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        loc = [-1, -1, -1]
        cnt = 0

        for i in range(n):
            if s[i] == 'a':
                loc[0] = i
            elif s[i] == 'b':
                loc[1] = i
            else:
                loc[2] = i

            cnt += 1 + min(loc)

        return cnt
