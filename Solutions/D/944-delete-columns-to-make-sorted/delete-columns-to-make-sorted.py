#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/delete-columns-to-make-sorted/description

# Time Complexity O(mn*log(n)), Space Complexity O(n)
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0

        for col in zip(*strs):
            if list(col) != sorted(col):
                cnt += 1

        return cnt
