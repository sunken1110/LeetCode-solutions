#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/zero-array-transformation-ii/description

# Complexity O(n*log(n))
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)


        def isPossible(idx):
            pref = [0] * (n+1)

            for q in queries[:idx]:
                l, r, val = q
                pref[l] += val
                pref[r+1] -= val

            psum = 0
            for i in range(n):
                psum += pref[i]
                
                if nums[i] > psum:
                    return False

            return True

        if not isPossible(m):
            return -1

        left, right = 0, m
        while left < right:
            mid = (left + right) // 2

            if isPossible(mid):
                right = mid

            else:
                left = mid + 1

        return right
