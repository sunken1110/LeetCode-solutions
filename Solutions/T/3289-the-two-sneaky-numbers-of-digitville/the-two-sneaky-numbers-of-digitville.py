#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        unique = set()

        for num in nums:
            if num not in unique:
                unique.add(num)

            else:
                ans.append(num)

        return ans
