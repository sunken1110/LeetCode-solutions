#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description

# Complexity O(n)
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s[:s.find(part)] + s[s.find(part) + len(part):]

        return s
