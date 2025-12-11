#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-square-sum-triples/description

# Time Complexity O(n^2), Space Complexity O(n)
class Solution:
    def countTriples(self, n: int) -> int:
        squares = set([s*s for s in range(1, n+1)])
        cnt = 0

        for a in range(1, n+1):
            for b in range(a+1, n+1):
                if a**2 + b**2 in squares:
                    cnt += 2

        return cnt
