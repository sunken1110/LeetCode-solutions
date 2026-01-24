#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description

# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        pairsum = set()
        nums.sort()

        for i in range(n // 2):
            pairsum.add(nums[i] + nums[n-i-1])

        return max(pairsum)
