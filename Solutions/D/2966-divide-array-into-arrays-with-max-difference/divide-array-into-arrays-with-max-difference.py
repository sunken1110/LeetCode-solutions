#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description

# Time Complexity O(n*log(n)), Space Complexity O(1)
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] <= k:
                ans.append(nums[i:i+3])

            else:
                return []

        return ans
