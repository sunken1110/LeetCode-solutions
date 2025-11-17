#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/number-of-substrings-with-only-1s/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        curr = 0
        mod = 10**9 + 7

        for num in s:
            if num == '1':
                curr += 1
                ans += curr

            else:
                curr = 0

        return ans % mod
