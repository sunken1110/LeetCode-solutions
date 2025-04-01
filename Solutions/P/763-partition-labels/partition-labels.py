#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/partition-labels/description

# Complexity O(n)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last_idx = [-1] * 26
        ans = []

        for idx, char in enumerate(s):
            alphabet = ord(char) - ord('a')
            last_idx[alphabet] = idx

        left = 0
        right = -1

        for idx, char in enumerate(s):
            alphabet = ord(char) - ord('a')
            right = max(right, last_idx[alphabet])

            if idx == right:
                ans.append(right - left + 1)
                left = idx + 1

        return ans
