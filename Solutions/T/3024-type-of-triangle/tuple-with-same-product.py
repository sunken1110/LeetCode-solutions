#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/type-of-triangle/description

# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()

        if nums[0] + nums[1] <= nums[2]:
            return 'none'

        elif nums[0] == nums[1] and nums[1] == nums[2]:
            return 'equilateral'

        elif nums[0] == nums[1] or nums[1] == nums[2]:
            return 'isosceles'

        else:
            return 'scalene'
