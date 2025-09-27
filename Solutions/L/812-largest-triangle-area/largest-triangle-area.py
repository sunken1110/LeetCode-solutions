#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/largest-triangle-area/description

# Time Complexity O(n^3), Space Complexity O(1)
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        area = 0

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    area = max(abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))), area)

        return area
