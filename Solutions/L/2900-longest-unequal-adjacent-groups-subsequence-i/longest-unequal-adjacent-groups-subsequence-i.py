#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        prev = -1
        ans = []

        for idx, num in enumerate(groups):
            if prev != num:
                ans.append(words[idx])
                prev = num

        return ans
