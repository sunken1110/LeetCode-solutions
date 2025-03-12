#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description

# Complexity O(log(n))
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1

            else:
                right = mid - 1

        if left < n and nums[left] > 0:
            return max(left, n - left)

        neg = left
        right = n-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == 0:
                left = mid + 1

            else:
                right = mid - 1

        return max(neg, n - left)
