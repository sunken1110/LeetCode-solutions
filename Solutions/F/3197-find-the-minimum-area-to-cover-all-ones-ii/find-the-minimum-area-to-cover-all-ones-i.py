#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/description

# Time Complexity O(m^2*n^2), Space Complexity O(m*n)
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def rotate(mat):
            m = len(mat)
            n = len(mat[0])

            return [[mat[i][j] for i in range(m-1, -1, -1)] for j in range(n)]


        def minArea(mat):
            if not mat or not mat[0]:
                return 0

            m = len(mat)
            n = len(mat[0])
            top, bottom, left, right = -1, m, n, -1

            for i in range(m):
                for j in range(n):
                    if mat[i][j]:
                        top = max(top, i)
                        bottom = min(bottom, i)
                        left = min(left, j)
                        right = max(right, j)

            if right == -1:
                return 0

            return (right-left+1) * (top-bottom+1)


        ans = float('inf')

        for _ in range(4):
            m = len(grid)
            n = len(grid[0])

            for i in range(1, m):
                area1 = minArea(grid[:i])

                for j in range(1, n):
                    partition2 = [row[:j] for row in grid[i:]]
                    partition3 = [row[j:] for row in grid[i:]]
                    area2 = minArea(partition2)
                    area3 = minArea(partition3)
                    ans = min(ans, area1 + area2 + area3)

                for k in range(i+1, m):
                    partition2 = grid[i:k]
                    partition3 = grid[k:]
                    area2 = minArea(partition2)
                    area3 = minArea(partition3)
                    ans = min(ans, area1 + area2 + area3)

            grid = rotate(grid)

        return ans
