#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/description

# Time Complexity O(n^2), Space Complexity O(n)
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        for i in range(n):
            j = i-1

            while j >= 0 and nums[j] | nums[i] != nums[j]:
                ans[j] = i-j+1
                nums[j] |= nums[i]
                j -= 1

        return ans
