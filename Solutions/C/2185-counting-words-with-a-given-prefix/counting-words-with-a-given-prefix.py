#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/counting-words-with-a-given-prefix/description

# Complexity O(n)
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        return len([word for word in words if word.startswith(pref)])
