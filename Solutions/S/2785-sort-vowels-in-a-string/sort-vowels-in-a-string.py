#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/sort-vowels-in-a-string/description

# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def sortVowels(self, s: str) -> str:
        t = list(s)
        vowels = []

        for char in s:
            if char in 'aeiouAEIOU':
                vowels.append(char)

        vowels.sort()
        order = 0
        
        for i in range(len(s)):
            if t[i] in 'aeiouAEIOU':
                t[i] = vowels[order]
                order += 1

        return ''.join(t)
