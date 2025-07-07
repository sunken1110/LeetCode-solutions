#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description

# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        cnt = 0
        start = -1
        idx = 0
        min_heap = []

        while idx < n or min_heap:
            if not min_heap:
                start = events[idx][0]

            while idx < n and events[idx][0] == start:
                heappush(min_heap, events[idx][1])
                idx += 1

            heappop(min_heap)
            cnt += 1
            start += 1

            while min_heap and min_heap[0] < start:
                heappop(min_heap)

        return cnt
