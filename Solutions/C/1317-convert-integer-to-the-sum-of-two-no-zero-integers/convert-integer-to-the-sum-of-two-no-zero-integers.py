#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if '0' not in str(i) and '0' not in str(n-i):
                return [str(i), str(n-i)]
