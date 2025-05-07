#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description

# Time Complexity O(m*n*log(m*n)), Space Complexity O(m*n)
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        times = [[inf] * n for _ in range(m)]
        times[0][0] = 0
        queue = [(0, 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            t, x, y = heappop(queue)

            if x == m-1 and y == n-1:
                return t
                
            if times[x][y] < t:
                continue

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    nt = max(t, moveTime[nx][ny]) + 1
                    if times[nx][ny] > nt:
                        times[nx][ny] = nt
                        heappush(queue, (times[nx][ny], nx, ny))
