#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description

# Complexity O(n^2)
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        cnt = 0

        for i in range(n):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    cnt += 1

        return cnt
