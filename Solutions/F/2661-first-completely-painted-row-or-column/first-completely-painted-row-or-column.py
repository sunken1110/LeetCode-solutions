#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/first-completely-painted-row-or-column/description

# Time Complexity O(n*m)
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        visited = {mat[row][col]: (row, col) for row in range(rows) 
                    for col in range(cols)}

        row_visited = [cols] * rows
        col_visited = [rows] * cols

        for idx, val in enumerate(arr):
            row, col = visited[val]
            row_visited[row] -= 1
            col_visited[col] -= 1

            if row_visited[row] == 0 or col_visited[col] == 0:
                return idx
