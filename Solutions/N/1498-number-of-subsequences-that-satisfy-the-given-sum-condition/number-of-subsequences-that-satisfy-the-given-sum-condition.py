#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description

# Time Complexity O(n*log(n)), Space Complexity O(1)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        l = 0
        r = n-1
        cnt = 0
        nums.sort()

        while l <= r:
            if nums[l] + nums[r] <= target:
                cnt += pow(2, r-l, mod)
                l += 1

            else:
                r -= 1

        return cnt % mod
