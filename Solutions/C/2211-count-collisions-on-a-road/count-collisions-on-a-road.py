#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-collisions-on-a-road/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip('L').rstrip('R')
        prev = 0
        collision = 0

        for d in directions:
            if d == 'L':
                collision += prev + 1
                prev = 0

            elif d == 'R':
                prev += 1

            else:
                collision += prev
                prev = 0
                
        return collision
