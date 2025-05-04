#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        unique = defaultdict(int)
        cnt = 0

        for i, j in dominoes:
            if i > j:
                i, j = j, i

            cnt += unique[(i, j)]
            unique[(i, j)] += 1

        return cnt
