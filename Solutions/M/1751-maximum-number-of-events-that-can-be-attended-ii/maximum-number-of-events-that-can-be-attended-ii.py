#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/description

# Time Complexity O(nk + n*log(n)), Space Complexity O(nk)
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        dp = [[0] * (k+1) for _ in range(len(events)+1)]

        for i, (start, end, val) in enumerate(events):
            prev = bisect_right(events, start-1, key=lambda x: x[1])

            for j in range(k):
                accept = dp[prev][j] + val
                skip = dp[i][j+1]
                dp[i+1][j+1] = accept if accept > skip else skip

        return dp[-1][-1]
