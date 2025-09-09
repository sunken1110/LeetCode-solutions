#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description

# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [i for i in range(1, n)] + [-(n-1)*n//2]
