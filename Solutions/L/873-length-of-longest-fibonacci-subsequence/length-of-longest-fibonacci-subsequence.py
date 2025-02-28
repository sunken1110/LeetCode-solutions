#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description

# Complexity O(n^2)
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        val2idx = {}
        ans = 0

        for idx, val in enumerate(arr):
            val2idx[val] = idx

        for i1 in range(1, n-1):
            f1 = arr[i1]

            for i2 in range(i1+1, n):
                f2 = arr[i2]
                f0 = f2 - f1

                if f0 >= f1:
                    break

                if f0 in val2idx:
                    i0 = val2idx[f0]
                    dp[i1][i2] = dp[i0][i1] + 1

                ans = max(ans, dp[i1][i2])

        return ans + 2 if ans > 0 else 0
