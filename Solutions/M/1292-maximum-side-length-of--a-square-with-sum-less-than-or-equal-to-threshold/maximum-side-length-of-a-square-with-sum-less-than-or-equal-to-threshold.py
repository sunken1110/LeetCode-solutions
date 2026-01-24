#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description

# Time Complexity O(m*n), Space Complexity O(m*n)
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def isValid(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    s = pref[i][j] - pref[i-k][j] - pref[i][j-k] + pref[i-k][j-k]

                    if s <= threshold:
                        return True

            return False

        
        m, n = len(mat), len(mat[0])
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        
        for i in range(m):
            row_sum = 0

            for j in range(n):
                row_sum += mat[i][j]
                pref[i+1][j+1] = pref[i][j+1] + row_sum

        for k in range(1, min(m, n) + 1):
            if isValid(k):
                ans = k

            else:
                break

        return ans
