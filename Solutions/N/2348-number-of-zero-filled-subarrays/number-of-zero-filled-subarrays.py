#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/number-of-zero-filled-subarrays/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        curr = 0

        for num in nums:
            if num == 0:
                curr += 1

            else:
                ans += curr*(curr+1)//2
                curr = 0

        return ans + curr*(curr+1)//2
