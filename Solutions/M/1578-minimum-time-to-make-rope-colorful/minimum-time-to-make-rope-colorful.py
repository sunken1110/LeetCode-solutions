#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = '-'
        curr_max = 0
        curr_time = 0
        ans = 0

        for i in range(len(colors)):
            if colors[i] == prev:
                curr_max = max(curr_max, neededTime[i])
                curr_time += neededTime[i]

            else:
                ans += curr_time - curr_max
                curr_max = neededTime[i]
                curr_time = neededTime[i]

            prev = colors[i]

        ans += curr_time - curr_max

        return ans
