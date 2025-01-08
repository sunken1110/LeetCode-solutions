#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/shifting-letters-ii/description

# Prefix Sum - Complexity O(n^2)
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        total_shift = [0] * (n+1)
        ans = []

        for start, end, direction in shifts:
            total_shift[start] += (1 if direction == 1 else -1)
            total_shift[end + 1] -= (1 if direction == 1 else -1)

        current_shift = 0 # prefix sum
        for i in range(n):
            current_shift += total_shift[i]
            ans.append(chr((ord(s[i]) - ord('a') + current_shift) % 26 + ord('a')))

        return ''.join(ans)


# Brute-force - Complexity O(n^2)
class Solution2:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        total_shift = [0] * len(s)
        ans = []

        for start, end, direction in shifts:
            for i in range(start, end + 1):
                total_shift[i] += (1 if direction == 1 else -1)

        for i, a in enumerate(s):
            ans.append(chr((ord(a) - ord('a') + total_shift[i]) % 26 + ord('a')))

        return ''.join(ans)
