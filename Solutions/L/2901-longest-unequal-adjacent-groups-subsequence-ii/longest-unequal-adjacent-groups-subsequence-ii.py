#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/description

# Time Complexity O(n^2), Space Complexity O(n^2)
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [[word] for word in words]


        def check(a, b):
            if len(a) != len(b):
                return False

            diff = 0

            for c1, c2 in zip(a, b):
                if c1 != c2:
                    diff += 1

            return diff == 1


        for i in range(1, n):
            for j in range(i):
                if groups[i] != groups[j] and check(words[i], words[j]) and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [words[i]]

        return max(dp, key=len)
