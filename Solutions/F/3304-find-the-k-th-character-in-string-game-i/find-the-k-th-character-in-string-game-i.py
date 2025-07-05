#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description

# Time Complexity O(log2(k)), Space Complexity O(k)
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'

        for _ in range(ceil(log2(k))):
            new = ''

            for char in word:
                new += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))

            word += new

        return word[k-1]
