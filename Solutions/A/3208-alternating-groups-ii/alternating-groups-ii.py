#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/alternating-groups-ii/description

# Complexity O(n)
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors = colors + colors[:k-1]
        cnt = 1
        ans = 0

        for i in range(len(colors)-1):
            if colors[i] != colors[i+1]:
                cnt += 1
            else:
                cnt = 1

            if cnt >= k:
                ans += 1

        return ans
