#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-original-typed-string-ii/description

# Time Complexity O(n+k*m), Space Complexity O(k) where m is a number of consecutive letters
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        blocks = []
        mod = 10**9 + 7
        cnt = 1

        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                cnt += 1

            else:
                blocks.append(cnt)
                cnt = 1

        blocks.append(cnt)
        total = 1

        for max_len in blocks:
            total = (total * max_len) % mod

        if len(blocks) >= k:
            return total

        dp = [0] * k
        dp[0] = 1

        for max_len in blocks:
            dp2 = [0] * k
            pref = 0

            for length in range(1, k):
                pref += dp[length-1]

                if length >= max_len + 1:
                    pref -= dp[length - max_len - 1]

                pref %= mod
                dp2[length] = pref

            dp = dp2

        return (total - sum(dp) % mod) % mod
