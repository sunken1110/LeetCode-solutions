#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-original-typed-string-i/description

# Time Complexity O(n), Space Complexity O(1)
class Solution1:
    def possibleStringCount(self, word: str) -> int:
        return sum(word[i] == word[i+1] for i in range(len(word)-1)) + 1


# Time Complexity O(n), Space Complexity O(1)
class Solution2:
    def possibleStringCount(self, word: str) -> int:
        prev = ''
        cnt = 0
        curr = 0

        for char in word:
            if prev != char:
                prev = char
                cnt += curr
                curr = 0

            else:
                curr += 1

        return cnt + curr + 1
