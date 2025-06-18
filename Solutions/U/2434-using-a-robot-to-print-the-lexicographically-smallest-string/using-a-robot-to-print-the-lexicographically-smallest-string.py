#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def robotWithString(self, s: str) -> str:
        pos = defaultdict(list)
        p = []
        stored = []
        prev = -1

        for idx, char in enumerate(s):
            pos[char].append(idx)

        for char in 'abcdefghijklmnopqrstuvwxyz':
            while stored and stored[-1] <= char:
                p.append(stored.pop())

            for idx in pos[char]:
                if idx > prev:
                    p.append(char)
                    stored.extend(s[prev+1:idx])
                    prev = idx

        p += reversed(stored)

        return ''.join(p)
