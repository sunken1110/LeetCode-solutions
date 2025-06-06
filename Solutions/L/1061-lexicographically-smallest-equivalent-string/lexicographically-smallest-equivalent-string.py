#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description

# Time Complexity O(m+n), Space Complexity O(n)
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        
        def union(x, y):
            x, y = find(x), find(y)

            if x == y:
                return

            if x > y:
                parent[x] = y

            else:
                parent[y] = x

        
        parent = [*range(26)]

        for c1, c2 in zip(s1, s2):
            i1 = ord(c1) - ord('a')
            i2 = ord(c2) - ord('a')
            union(i1, i2)

        return ''.join(chr(find(ord(c) - ord('a')) + ord('a')) for c in baseStr)
