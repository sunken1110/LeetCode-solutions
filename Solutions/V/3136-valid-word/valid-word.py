#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/valid-word/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        nums = '0123456789'
        vowels = 'aeiouAEIOU'
        consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        target = nums + vowels + consonants
        cnt_vowel = 0
        cnt_consonant = 0

        for char in word:
            if char not in target:
                return False

            elif char in vowels:
                cnt_vowel += 1

            elif char in consonants:
                cnt_consonant += 1

        if cnt_vowel >= 1 and cnt_consonant >= 1:
            return True

        else:
            return False
