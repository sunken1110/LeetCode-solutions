#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/clear-digits/description

# Complexity O(n)
class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []

        for char in s:
            if char.isdigit():
                if ans:
                    ans.pop()

            else:
                ans.append(char)

        return ''.join(ans)
