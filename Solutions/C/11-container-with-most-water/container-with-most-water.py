#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/container-with-most-water/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        vol = 0

        while left < right:
            vol = max(vol, (right-left) * min(height[left], height[right]))
        
            if height[left] <= height[right]:
                left += 1

            else:
                right -= 1

        return vol
