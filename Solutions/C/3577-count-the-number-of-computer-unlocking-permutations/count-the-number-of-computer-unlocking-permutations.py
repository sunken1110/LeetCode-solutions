#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)

        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0

        ans = 1
        mod = 10**9 + 7

        for i in range(2, n):
            ans = (ans * i) % mod

        return ans
