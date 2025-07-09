#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description

# Time Complexity O(n), Space Complexity O(n)
class Solution1:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        sums = list(accumulate(nums, initial=0))

        return max(sums) - min(sums)


# Time Complexity O(n), Space Complexity O(n)
class Solution2:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        maxSub = -inf
        minSub = inf
        
        sumSub = 0
        for i in range(n):
            sumSub = max(0, sumSub + nums[i])
            maxSub = max(maxSub, sumSub)

        sumSub = 0
        for i in range(n-1, -1, -1):
            sumSub = min(0, sumSub + nums[i])
            minSub = min(minSub, sumSub)

        return max(abs(maxSub), abs(minSub))
