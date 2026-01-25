#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description

# Time Complexity O(n*log(n)), Space Complexity O(1)
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        min_diff = nums[k-1] - nums[0]

        for i in range(1, n-k+1):
            min_diff = min(min_diff, nums[i+k-1]-nums[i])

        return min_diff
