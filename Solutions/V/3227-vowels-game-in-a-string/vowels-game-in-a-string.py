#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/vowels-game-in-a-string/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(char in 'aeiou' for char in s)
