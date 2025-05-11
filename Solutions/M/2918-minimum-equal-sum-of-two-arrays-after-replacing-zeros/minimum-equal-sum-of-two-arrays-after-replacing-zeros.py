#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)
        sum1 = sum(nums1) + zero1
        sum2 = sum(nums2) + zero2

        if (sum1 > sum2 and zero2 == 0) or (sum1 < sum2 and zero1 == 0):
            return -1

        return max(sum1, sum2)
