#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description

# Time Complexity O(mn*log(m)), Space Complexity O(mn)
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        anagram = [''.join(sorted(word)) for word in words]
        ans = [words[0]]

        for i in range(len(words)-1):
            if anagram[i] != anagram[i+1]:
                ans.append(words[i+1])

        return ans
