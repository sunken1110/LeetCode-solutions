#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description

# Complexity O(n)
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(int)
        pair = {}
        ans = []

        for b, c in queries:
            if b in pair:
                c0 = pair[b]
                colors[c0] -= 1

                if colors[c0] == 0:
                    colors.pop(c0)

            pair[b] = c
            colors[c] += 1

            ans.append(len(colors))

        return ans
