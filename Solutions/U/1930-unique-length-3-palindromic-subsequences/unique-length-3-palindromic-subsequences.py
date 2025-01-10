#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description

# Complexity O(n)
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        cnt = 0

        for c in 'abcdefghijklmnopqrstuvwxyz':
            l, r = s.find(c), s.rfind(c)

            if l != -1 and r != -1:
                cnt += len(set(s[l+1:r]))

        return cnt
