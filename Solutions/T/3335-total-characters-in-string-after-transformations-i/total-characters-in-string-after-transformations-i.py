#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description

# Time Complexity O(n+t), Space Complexity O(1)
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = deque([0] * 26)
        mod = 10**9 + 7

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        for _ in range(t):
            cnt[0] += cnt[25] % mod
            cnt.appendleft(cnt.pop())

        return sum(cnt) % mod
