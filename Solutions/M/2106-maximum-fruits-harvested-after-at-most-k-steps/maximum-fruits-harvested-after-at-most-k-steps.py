#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        max_val = 0
        val = 0
        l = 0

        for r in range(n):
            val += fruits[r][1]

            while l <= r:
                pos_l = fruits[l][0]
                pos_r = fruits[r][0]
                dist = min(abs(startPos - pos_l) + (pos_r - pos_l),
                            abs(startPos - pos_r) + (pos_r - pos_l))

                if dist > k:
                    val -= fruits[l][1]
                    l += 1

                else:
                    break

            max_val = max(max_val, val)

        return max_val
