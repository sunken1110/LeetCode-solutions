#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/delete-characters-to-make-fancy-string/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = ''
        cnt = 0
        ans = ''

        for char in s:
            if char == prev:
                if cnt != 2:
                    ans += char
                    cnt += 1

            else:
                prev = char
                cnt = 1
                ans += char

        return ans
