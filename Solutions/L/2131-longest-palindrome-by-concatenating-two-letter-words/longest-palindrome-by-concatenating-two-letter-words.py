#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = Counter(words)
        length = 0
        middle = 0

        for word, val in freq.items():
            pal = word[::-1]

            if pal == word:
                length += (val // 2) * 4

                if val % 2 == 1:
                    middle = 2

            elif pal > word and pal in freq:
                length += min(val, freq[pal]) * 4

        return length + middle
