#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-operations-to-obtain-zero/description

# Time Complexity O(log(max(num1, num2))), Space Complexity O(1)
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0

        while num1 and num2:
            q, r = divmod(num1, num2)
            ans += q
            num1, num2 = num2, r

        return ans
