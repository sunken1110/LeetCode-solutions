#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ones = []

        for idx, num in enumerate(s[::-1]):
            if num == '1':
                ones.append(idx)

        i = 0
        ans = len(s) - len(ones)

        while i < len(ones) and k - 2**ones[i] >= 0:
            k -= 2**ones[i]
            i += 1
            ans += 1

        return ans
