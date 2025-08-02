#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description

# Time Complexity O(n), Space Complexityt O(n)
class Solution:
    def maxSum(self, nums: List[int]) -> int:        
        unique = set()
        ans = 0

        for num in nums:
            if num > 0 and num not in unique:
                ans += num
                unique.add(num)

        return ans if ans != 0 else max(nums)
