#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/maximum-erasure-value/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = 0
        max_score = 0
        unique = set()
        l = 0

        for num in nums:
            while num in unique:
                unique.remove(nums[l])
                score -= nums[l]
                l += 1

            unique.add(num)
            score += num
            max_score = max(max_score, score)

        return max_score
