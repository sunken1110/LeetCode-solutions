#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description

# Complexity O(n*log(n))
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xcoord = []
        ycoord = []

        for x1, y1, x2, y2 in rectangles:
            xcoord.append((x1, x2))
            ycoord.append((y1, y2))


        def valid_cut(coords):
            coords.sort()
            cnt = -1
            prev_z2 = 0

            for z1, z2 in coords:
                if z1 < prev_z2:
                    prev_z2 = max(prev_z2, z2)

                else:
                    cnt += 1
                    
                    if cnt >= 2:
                        return True

                    prev_z2 = z2

            return False
            

        return valid_cut(xcoord) or valid_cut(ycoord)
