#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description

# Time Complexity O(n), Space Complexity O(k^2)
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]

        for num in nums:
            num %= k

            for mod in range(k):
                dp[num][mod] = dp[mod][num] + 1

        return max(map(max, dp))
