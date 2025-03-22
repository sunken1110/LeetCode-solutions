#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-missing-and-repeated-values/description

# Complexity O(n^2)
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        missing = (n**2) * (n**2 + 1) // 2
        check = set()

        for row in grid:
            for num in row:
                if num not in check:
                    check.add(num)
                    missing -= num

                else:
                    twice = num

        return [twice, missing]
