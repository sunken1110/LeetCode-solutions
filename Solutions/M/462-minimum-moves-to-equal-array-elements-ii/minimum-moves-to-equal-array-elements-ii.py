#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description

# Complexity O(n*log(n))
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]

        return sum([abs(mid - num) for num in nums])
