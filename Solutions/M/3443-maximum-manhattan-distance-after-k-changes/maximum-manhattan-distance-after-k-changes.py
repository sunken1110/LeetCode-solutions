#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/description

# Time Complexity O(n), Space Complexityt O(1)
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        dirs = defaultdict(int)
        max_dist = 0

        for idx, move in enumerate(s):
            dirs[move] += 1
            dist = abs(dirs['N'] - dirs['S']) + abs(dirs['E'] - dirs['W']) + 2*k
            max_dist = max(max_dist, min(dist, idx+1))

        return max_dist
