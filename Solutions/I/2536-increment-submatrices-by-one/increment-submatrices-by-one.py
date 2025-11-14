#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/increment-submatrices-by-one/description

# Time Complexity O(n^2), Space Complexity O(n^2)
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        pref_mat = [[0] * (n+1) for _ in range(n+1)]

        for r1, c1, r2, c2 in queries:
            pref_mat[r1][c1] += 1
            pref_mat[r2+1][c1] -= 1
            pref_mat[r1][c2+1] -= 1
            pref_mat[r2+1][c2+1] += 1

        for row in range(n):
            for col in range(n):
                loc1 = 0 if row == 0 else mat[row-1][col]
                loc2 = 0 if col == 0 else mat[row][col-1]
                loc3 = 0 if (row == 0 or col == 0) else mat[row-1][col-1]
                mat[row][col] = pref_mat[row][col] + loc1 + loc2 - loc3

        return mat
