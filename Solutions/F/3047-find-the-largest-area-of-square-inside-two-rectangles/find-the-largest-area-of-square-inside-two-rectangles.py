#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/description

# Time Complexity O(n^2), Space Complexity O(1)
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        square = 0

        for i in range(n-1):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]

            for j in range(i+1, n):
                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]

                width = min(x2, x4) - max(x1, x3)
                height = min(y2, y4) - max(y1, y3)

                if width > 0 and height > 0 and min(width, height) > square:
                    square = min(width, height)

        return square ** 2
