#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/word-subsets/description

# Complexity O(n + m)
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universal = []
        freq = {}
        for word in words2:
            for char, n in Counter(word).items():
                if char not in freq or freq[char] < n:
                    freq[char] = n

        for word in words1:
            cnt = Counter(word)
            subset = True
            for char, n in freq.items():
                if char not in cnt or n > cnt[char]:
                    subset = False
                    break

            if subset:
                universal.append(word)

        return universal
