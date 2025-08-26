#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/diagonal-traverse/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        row, col = 0, 0
        ans = []

        for _ in range(m*n):
            ans.append(mat[row][col])

            if (row + col) % 2 == 0:
                if col == n-1:
                    row += 1

                elif row == 0:
                    col += 1

                else:
                    row -= 1
                    col += 1

            else:
                if row == m-1:
                    col += 1

                elif col == 0:
                    row += 1

                else:
                    row += 1
                    col -= 1

        return ans
