#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/meeting-rooms-iii/description

# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = list(range(n))
        cnt = [0] * n
        booked = []

        for start, end in meetings:
            while booked and booked[0][0] <= start:
                heappush(rooms, heappop(booked)[1])

            gap = end - start

            if rooms:
                room = heappop(rooms)
                curr = start

            else:
                curr, room = heappop(booked)

            heappush(booked, (curr + gap, room))
            cnt[room] += 1

        return max(range(n), key=lambda x: cnt[x])
