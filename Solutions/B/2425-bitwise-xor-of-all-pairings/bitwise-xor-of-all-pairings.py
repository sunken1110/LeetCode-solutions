#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/bitwise-xor-of-all-pairings/description

# Complexity O(n)
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        if len(nums1) % 2 != 0:
            for num in nums2:
                ans ^= num

        if len(nums2) % 2 != 0:
            for num in nums1:
                ans ^= num

        return ans
