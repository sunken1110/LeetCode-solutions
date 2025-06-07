#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)
        min_heap = []

        for idx, char in enumerate(s):
            if char == '*':
                s[-heappop(min_heap)[1]] = '*'

            else:
                heappush(min_heap, (char, -idx))

        return ''.join(s).replace('*', '')
