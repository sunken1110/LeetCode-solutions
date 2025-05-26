#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-words-containing-character/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []

        for idx, word in enumerate(words):
            if x in word:
                ans.append(idx)

        return ans
