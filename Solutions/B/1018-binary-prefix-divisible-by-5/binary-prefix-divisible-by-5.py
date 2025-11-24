#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/binary-prefix-divisible-by-5/description

# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        curr = 0

        for bit in nums:
            curr = (curr * 2 + bit) % 5
            ans.append(curr == 0)

        return ans
