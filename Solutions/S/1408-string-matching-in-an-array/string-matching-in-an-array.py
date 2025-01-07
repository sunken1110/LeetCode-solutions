#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/string-matching-in-an-array/description

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        long_word = ' '.join(words)

        for word in words:
            if long_word.count(word) > 1:
                ans.append(word)

        return ans

