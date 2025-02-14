#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description

# Complexity O(n*log(n))
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ans = 0

        for i in range(len(nums)):
            x = heappop(nums)
   
            if x < k:
                y = heappop(nums)
                z = x*2 + y if x < y else y*2 + x
                heappush(nums, z)
                ans += 1

            else:
                break

        return ans
