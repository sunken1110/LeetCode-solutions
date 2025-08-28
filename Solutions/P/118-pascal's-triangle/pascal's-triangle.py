#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/pascals-triangle/description

# Time Complexity O(n^2), Space Complexity O(1)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[] for _ in range(numRows)]

        for i in range(numRows):
            for j in range(i+1):
                pascal[i].append(comb(i, j))

        return pascal
