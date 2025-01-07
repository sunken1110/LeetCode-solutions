#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        long_word = ' '.join(words)

        for word in words:
            if long_word.count(word) > 1:
                ans.append(word)

        return ans

