#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0

        for num in nums:
            if num % 3 != 0:
                cnt += 1

        return cnt
