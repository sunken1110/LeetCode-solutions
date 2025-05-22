#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/set-matrix-zeroes/description

# Time Complexity O(m*n), Space Complexity O(m*n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        pos = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    pos.add((i, j))

        for i, j in pos:
            matrix[i] = [0] * n
            
            for row in matrix:
                row[j] = 0
