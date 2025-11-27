#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/set-intersection-size-at-least-two/description

# Time Complexity O(n*log(n)), Space Complexity O(1)
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        a, b = -1, -1
        ans = 0

        for l, r in intervals:
            if l > b:
                a = r-1
                b = r
                ans += 2

            elif l > a:
                a = b
                b = r
                ans += 1

        return ans
