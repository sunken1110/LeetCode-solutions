#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-days-without-meetings/description

# Complexity O(n*log(n))
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        prev_end = 0
        cnt = 0

        meetings.sort()

        for start, end in meetings:
            if start > prev_end + 1:
                cnt += start - prev_end - 1

            prev_end = max(prev_end, end)

        cnt += days - prev_end

        return cnt
