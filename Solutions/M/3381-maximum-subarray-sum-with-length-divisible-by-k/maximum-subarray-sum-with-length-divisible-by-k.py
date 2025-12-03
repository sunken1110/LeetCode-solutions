#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = 0
        dp = [inf] * (k-1) + [0]
        ans = -inf

        for idx, num in enumerate(nums):
            pref += num
            ans = max(ans, pref - dp[idx%k])
            dp[idx%k] = min(pref, dp[idx%k])

        return ans
