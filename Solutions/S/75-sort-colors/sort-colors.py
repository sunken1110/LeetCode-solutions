#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/sort-colors/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mapping = defaultdict(int)

        for num in nums:
            mapping[num] += 1

        idx = 0

        for color in range(3):
            while mapping[color] > 0:
                nums[idx] = color
                idx += 1
                mapping[color] -= 1
