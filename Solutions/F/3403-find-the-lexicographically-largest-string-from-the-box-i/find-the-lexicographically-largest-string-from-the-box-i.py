#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        n = len(word)
        max_length = n - numFriends + 1
        ans = 'a'

        for i in range(n):
            curr = word[i:i+max_length]

            if ans < curr:
                ans = curr
        
        return ans
