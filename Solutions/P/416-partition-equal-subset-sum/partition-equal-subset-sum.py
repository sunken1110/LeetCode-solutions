#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/partition-equal-subset-sum/description

# Time Complexity O(n*sum(nums)), Space Complexity O(sum(nums))
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        q, r = sum(nums) // 2, sum(nums) % 2

        if r == 1:
            return False

        dp = [False] * (q+1)
        dp[q] = True

        for num in nums:
            for i in range(q-num+1):
                dp[i] = dp[i] or dp[i+num]

        return dp[0]
