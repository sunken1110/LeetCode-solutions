#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description

# Time Complexity O(n*log(n))
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        r = grid[0][0] % x
        arr = []

        for row in grid:
            for num in row:
                if r != num % x:
                    return -1

                arr.append(num)

        arr.sort()
        mid = arr[len(arr) // 2]

        return sum([abs(num - mid) for num in arr]) // x
