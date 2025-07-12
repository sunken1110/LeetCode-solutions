#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []
        prev = 0

        for i in range(n):
            gaps.append(startTime[i] - prev)
            prev = endTime[i]

        gaps.append(eventTime - prev)
        free = sum(gaps[:k+1])
        max_free = free

        for i in range(n-k):
            free += gaps[i+k+1] - gaps[i]
            max_free = max(max_free, free)

        return max_free
