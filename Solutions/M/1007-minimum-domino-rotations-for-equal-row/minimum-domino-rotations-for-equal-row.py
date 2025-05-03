#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:        
        def rotate(val, A, B):
            cnt = 0

            for a, b in zip(A, B):
                if a == val:
                    continue

                elif b == val:
                    cnt += 1

                else:
                    return inf

            return cnt
            

        n = len(tops)
        check = {tops[0], bottoms[0]}
        cnt = inf

        for val in check:
            cnt = min(cnt, rotate(val, tops, bottoms), rotate(val, bottoms, tops))

        return cnt if cnt != inf else -1
