#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description

# Time Complexity O(n^2), Space Complexity O(1)
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            check = False

            for i in range(num):
                if i | (i+1) == num:
                    ans.append(i)
                    check = True
                    break

            if not check:
                ans.append(-1)

        return ans
