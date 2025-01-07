#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/string-matching-in-an-array/description

# Complexity O(n^2)
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        long_word = ' '.join(words)

        for word in words:
            if long_word.count(word) > 1:
                ans.append(word)

        return ans


# Brute-force - Complexity O(n^2)
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = []

        for i in range(n):
            for j in range(n):
                if j != i and words[i] in words[j]:
                    ans.append(words[i])
                    break

        return ans
