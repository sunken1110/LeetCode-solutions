#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/description

# Time Complexity O(n^2), Space Complexity O(1)
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        n = len(points)
        cnt = 0

        for i in range(n-1):
            x, y = points[i]
            prev_y = -inf

            for j in range(i+1, n):
                if prev_y < points[j][1] <= y:
                    cnt += 1
                    prev_y = points[j][1]

                elif prev_y >= y:
                    break

        return cnt
